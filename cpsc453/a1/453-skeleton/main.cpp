#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include <iostream>

#include "Geometry.h"
#include "GLDebug.h"
#include "Log.h"
#include "ShaderProgram.h"
#include "Shader.h"
#include "Window.h"
#include "AssetPath.h"


int depth = 0;
int type = 0;

// EXAMPLE CALLBACKS
class MyCallbacks : public CallbackInterface {

public:
	MyCallbacks(ShaderProgram& shader) : shader(shader) {}

	virtual void keyCallback(int key, int scancode, int action, int mods) {
		if (key == GLFW_KEY_R && action == GLFW_PRESS) { // On a positive edge press (when FIRST clicked)
			shader.recompile();
		}
		if (key == GLFW_KEY_UP && action == GLFW_PRESS) { // Up key increases depth
            depth++;
		}
		if (key == GLFW_KEY_DOWN && action == GLFW_PRESS) { // Down decreases depth
            depth--;
		}
	}

	// Other callbacks we implemented that you may use
	//virtual void mouseButtonCallback(int button, int action, int mods) {}
	//virtual void cursorPosCallback(double xpos, double ypos) {}
	//virtual void scrollCallback(double xoffset, double yoffset) {}
	//virtual void windowSizeCallback(int width, int height) { CallbackInterface::windowSizeCallback(width, height);/*Should be called*/ }

private:
	ShaderProgram& shader;
};

class MyCallbacks2 : public CallbackInterface {

public:
	MyCallbacks2() {}

	virtual void keyCallback(int key, int scancode, int action, int mods) {
		if (key == GLFW_KEY_R && action == GLFW_PRESS) {
			std::cout << "called back" << std::endl;
		}
	}
};
// END EXAMPLES

// SIERPINSKI METHODS
void draw_triangle(glm::vec3 a,glm::vec3 b,glm::vec3 c, CPU_Geometry& cpu, GPU_Geometry& gpu){
    // vertices
    cpu.verts.push_back(a);
    cpu.verts.push_back(b);
    cpu.verts.push_back(c);

    // colours (these should be in linear space)
    cpu.cols.push_back(glm::vec3(1.f, 0.f, 0.f)); // Red
    cpu.cols.push_back(glm::vec3(0.f, 1.f, 0.f)); // Green
    cpu.cols.push_back(glm::vec3(0.f, 0.f, 1.f)); // Blue

    gpu.setCols(cpu.cols); // Upload vertex colour attribute to VBO
    gpu.setVerts(cpu.verts); // Upload vertex position geometry to VBO
}

void divide_triangle(glm::vec3 a,glm::vec3 b, glm::vec3 c, int m, CPU_Geometry& cpu, GPU_Geometry& gpu){
    glm::vec3 v0,v1,v2;
    int j;
    if (m > 0) {
        for (j = 0; j < 2; j++)
            v0[j] = (a[j]+b[j])*0.5;
        for (j = 0; j < 2; j++)
            v1[j] = (a[j]+c[j])*0.5;
        for (j = 0; j < 2; j++)
            v2[j] = (b[j]+c[j])*0.5;
        divide_triangle(a, v0, v1, m-1,cpu,gpu);
        divide_triangle(c, v1, v2, m-1,cpu,gpu);
        divide_triangle(b, v2, v0, m-1,cpu,gpu);
    }
    else{
        draw_triangle(a, b, c,cpu,gpu);
    }
}

// MERGER SPONGE METHODS
void draw_square(glm::vec3 a, glm::vec3 b,glm::vec3 c, glm::vec3 d, CPU_Geometry& cpu, GPU_Geometry& gpu){

}

void draw_square(glm::vec3 a, glm::vec3 b,glm::vec3 c, glm::vec3 d, int m, CPU_Geometry& cpu, GPU_Geometry& gpu){
    glm::vec3 v0,v1,v2,v3;
    int j;
    if (m > 0) {
        for (j = 0; j < 2; j++)
            v0[j] = (a[j]+b[j])/3;
        for (j = 0; j < 2; j++)
            v1[j] = (a[j]+c[j])/3;
        for (j = 0; j < 2; j++)
            v2[j] = (b[j]+c[j])/3;
        for (j = 0; j < 2; j++)
            v3[j] = (b[j]+c[j])/3;
        divide_triangle(a, v0, v1, m-1,cpu,gpu);
        divide_triangle(c, v1, v2, m-1,cpu,gpu);
        divide_triangle(b, v2, v0, m-1,cpu,gpu);
    }
    else{
        draw_triangle(a, b, c,cpu,gpu);
    }
}

int main() {
	Log::debug("Starting main");

	// WINDOW
	glfwInit();//MUST call this first to set up environment (There is a terminate pair after the loop)
	Window window(800, 800, "CPSC 453 Assignment 1: Fractals"); // Can set callbacks at construction if desired

	GLDebug::enable(); // ON Submission you may comments this out to avoid unnecessary prints to the console

	// SHADERS
	ShaderProgram shader(
		AssetPath::Instance()->Get("shaders/basic.vert"), 
		AssetPath::Instance()->Get("shaders/basic.frag")
	); // Render pipeline we will use (You can use more than one!)

	// CALLBACKS
	std::shared_ptr<MyCallbacks> callback_ptr = std::make_shared<MyCallbacks>(shader); // Class To capture input events
	//std::shared_ptr<MyCallbacks2> callback2_ptr = std::make_shared<MyCallbacks2>();
	window.setCallbacks(callback_ptr); // Can also update callbacks to new ones as needed (create more than one instance)

	// // GEOMETRY
	CPU_Geometry cpu; // Just a collection of vectors
	GPU_Geometry gpu; // Wrapper managing VAO and VBOs, in a TIGHTLY packed format
	// //https://www.khronos.org/opengl/wiki/Vertex_Specification_Best_Practices#Attribute_sizes


	// RENDER LOOP
	while (!window.shouldClose()) {
		glfwPollEvents(); // Propagate events to the callback class

		shader.use(); // Use "this" shader to render
		gpu.bind(); // USe "this" VAO (Geometry) on render call

        // Fix anticlockwise triangles
        glDisable(GL_CULL_FACE);

		glEnable(GL_FRAMEBUFFER_SRGB); // Expect Colour to be encoded in sRGB standard (as opposed to RGB) 
		// https://www.viewsonic.com/library/creative-work/srgb-vs-adobe-rgb-which-one-to-use/
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); // Clear render screen (all zero) and depth (all max depth)
        //glDeleteBuffers();

        //depth=2;

        if (type==0){
            divide_triangle(
                glm::vec3(-0.5f, -0.5f, 0.f),
                glm::vec3(0.5f, -0.5f, 0.f),
                glm::vec3(0.f, 0.5f, 0.f),
                depth,cpu,gpu
            );

            for (int i=0; i<pow(3,depth);i++){
                glDrawArrays(GL_TRIANGLES,3*i,3);
            }
        }

		glDisable(GL_FRAMEBUFFER_SRGB); // disable sRGB for things like imgui (if used)

		window.swapBuffers(); //Swap the buffers while displaying the previous 
	}

	glfwTerminate(); // Clean up GLFW
	return 0;
}
