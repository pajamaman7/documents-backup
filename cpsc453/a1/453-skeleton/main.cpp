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
		if (key == GLFW_KEY_RIGHT&& action == GLFW_PRESS && type < 6) { // Right key changes type (max 7)
            type++;
		}
		if (key == GLFW_KEY_LEFT && action == GLFW_PRESS && type > 0) { // Left key changes type (min 0)
            type--;
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

// SIERPINSKI FUNCTIONS
void draw_triangle(glm::vec3 a,glm::vec3 b,glm::vec3 c, glm::vec3 color, CPU_Geometry& cpu, GPU_Geometry& gpu){
    // vertices
    cpu.verts.push_back(a);
    cpu.verts.push_back(b);
    cpu.verts.push_back(c);

    // colours (these should be in linear space)
    cpu.cols.push_back(color); 
    cpu.cols.push_back(color); 
    cpu.cols.push_back(color); 

    //Add data to gpu
    gpu.setCols(cpu.cols);
    gpu.setVerts(cpu.verts);
    //Draw current triangle
    glDrawArrays(GL_TRIANGLES,0,3);
    //Clear verts,cols for memory etc
    cpu.verts.clear();
    cpu.cols.clear();
}

void divide_triangle(glm::vec3 a,glm::vec3 b, glm::vec3 c, int m, CPU_Geometry& cpu, GPU_Geometry& gpu){
    glm::vec3 v0,v1,v2;
    if (m > 0) {
        //Extra points created as midpoints between a,b,c
        v0 = (a + b) * 0.5f; 
        v1 = (a + c) * 0.5f;
        v2 = (b + c) * 0.5f;
        //Recursive calls for the three smaller triangles
        divide_triangle(a, v0, v1, m-1,cpu,gpu);
        divide_triangle(c, v1, v2, m-1,cpu,gpu);
        divide_triangle(b, v2, v0, m-1,cpu,gpu);
    }
    else{
        // blue-green gradient based on position of a
        glm::vec3 color = glm::vec3(0.f,a[0]+1, a[1]+1);
        draw_triangle(a, b, c, color,cpu,gpu);
    }
}

// MENGER SPONGE FUNCTIONS
void draw_square(glm::vec3 a, glm::vec3 b, glm::vec3 color, CPU_Geometry& cpu, GPU_Geometry& gpu){
    // Takes in the top left and bottom right corner, as well as color and gpu,cpu, draws two triangles to make a square
    draw_triangle( a, glm::vec3(b[0],a[1],0.f),b,color, cpu,gpu);
    draw_triangle( a,b, glm::vec3(a[0],b[1],0.f),color,cpu,gpu);
}

void divide_square(glm::vec3 a, glm::vec3 b, int m, CPU_Geometry& cpu, GPU_Geometry& gpu){
    // Size counter to calculate subdivided squares
    float size = (b[0]-a[0])/3.f;
    if (m > 0) {
        //iterates over a 3x3 grid
        for(int i=0; i<3; i++){
            for(int j=0; j<3; j++){
                if(i!=1||j!=1){ // Skip middle square
                    // TODO weird offset
                    float x = a[0]+i*size;
                    float y = a[1]+j*size;
                    //recursive call
                    divide_square(glm::vec3(x,y,0.f),glm::vec3(x+size,y+size,0.f),m-1,cpu,gpu);
                }
            }
        }
    }
    else{
        // blue-red gradient based on corner position
        glm::vec3 color = glm::vec3(a[0]+1, 0.f, a[1]+0.75f);
        draw_square(a, b, color, cpu, gpu);
    }
}

//PYTHAGORAS FUNCTIONS
//This method takes in the two base sides, compared to the square function which takes opposite corners
void draw_leaf(glm::vec3 a, glm::vec3 b, CPU_Geometry& cpu, GPU_Geometry& gpu){
    // General Side length 
    glm::vec3 ab = b-a;
    float size = glm::length(ab);

    //Compute the color, so that smaller leaves are greener and bigger ones are brown
    glm::vec3 brown = glm::vec3(0.5f,0.2f,0.f);
    glm::vec3 green = glm::vec3(0.f,1.f,0.f);
    glm::vec3 color = 2*size*brown+(1-2*size)*green;

    // find the other verticies from a,b
    glm::vec3 perp = glm::vec3(-ab[1],ab[0],0.f);
    glm::vec3 c = b+perp;
    glm::vec3 d = a+perp;

    //Draw the two triangles to make the square
    draw_triangle(a,b,c,color,cpu,gpu);
    draw_triangle(c,d,a,color,cpu,gpu);
}
void pythagoras(glm::vec3 a, glm::vec3 b, int m, CPU_Geometry& cpu, GPU_Geometry& gpu){
    if(m<0) return;
    draw_leaf(a,b,cpu,gpu);
    glm::vec3 ab = b-a;
    glm::vec3 mid = (b+a)/2.f;

    glm::vec3 perp= glm::vec3(-ab[1],ab[0],0.f);

    glm::vec3 c = mid+3.f*perp/2.f;
    pythagoras(a+perp,c,m-1,cpu,gpu);
    pythagoras(c,b+perp,m-1,cpu,gpu);
}


//LINE FUNCTION
void draw_line(glm::vec3 a, glm::vec3 b,glm::vec3 color, CPU_Geometry& cpu, GPU_Geometry& gpu){
    // vertices
    cpu.verts.push_back(a);
    cpu.verts.push_back(b);

    // colours (these should be in linear space)
    cpu.cols.push_back(color); 
    cpu.cols.push_back(color); 

    //Add data to gpu
    gpu.setCols(cpu.cols);
    gpu.setVerts(cpu.verts);
    //Draw current triangle
    glDrawArrays(GL_LINES,0,3);
    //Clear verts,cols for memory etc
    cpu.verts.clear();
    cpu.cols.clear();
}

// KOCH FUNCTIONS
void koch_line(glm::vec3 a, glm::vec3 e, int m, CPU_Geometry& cpu, GPU_Geometry& gpu){
    //Pick color based on a
    glm::vec3 color = glm::vec3(a[1]+0.5f,a[0]+0.5f,1.f);
    if(m>0){
        glm::vec3 b= (2.f*a+e)/3.f;
        glm::vec3 d= (a+2.f*e)/3.f;

        // make vector from b to d and its midpoint
        glm::vec3 bd = d - b;
        glm::vec3 mid = (b + d) * 0.5f;
        
        // Find normal perp vector to bd and add to midpoint
        glm::vec3 perp = glm::vec3(-bd[1], bd[0], 0.0f); 
        glm::vec3 c = mid + perp;
        
        // Draw all four lines
        koch_line(a,b,m-1,cpu,gpu);
        koch_line(b,c,m-1,cpu,gpu);
        koch_line(c,d,m-1,cpu,gpu);
        koch_line(d,e,m-1,cpu,gpu);
    } else{
        draw_line(a,e,color,cpu,gpu);
    }
}

void dragon(glm::vec3 a, glm::vec3 c, int m, CPU_Geometry& cpu, GPU_Geometry& gpu){
    if(m>0 ){
        glm::vec3 mid = (a + c) * 0.5f;
        glm::vec3 ac = c - a;

        //Compute the midpoint and perpendicular vector to use (in order to compute c)
        glm::vec3 perp = glm::vec3(-ac[1], ac[0], 0.0f); 
        glm::vec3 b = mid - perp/2.f;

        //These line directions are important, they choose which way the fractal folds on each iteration
        dragon(a,b,m-1,cpu,gpu);
        dragon(c,b,m-1,cpu,gpu);
    }
    else{
        //pick color based on coordinates
        glm::vec3 color = glm::vec3(a[0]+1,c[1]+1,0.f);
        draw_line(a,c,color,cpu,gpu);
    }
}

// Hilbert curve implementation
void draw_cup(glm::vec3 a, glm::vec3 b, CPU_Geometry& cpu, GPU_Geometry& gpu){
    //compute vector across opening
    glm::vec3 ab = b-a;
    // make perp vector for the hundredth time
    glm::vec3 perp = glm::vec3(-ab[1],ab[0],0.f);
    // c is adjacent to b, d is ajdacent to a
    glm::vec3 c = b-perp;
    glm::vec3 d = a-perp;

    // COLOR YAY
    glm::vec3 color = glm::vec3(0.f,a[0],a[1]);
    //debug: use white 
    color = glm::vec3(1,1,1);
    draw_line(a,d,color,cpu,gpu);
    draw_line(d,c,color,cpu,gpu);
    draw_line(c,b,color,cpu,gpu);
}

void hilbert(glm::vec3 a, glm::vec3 d, int m, CPU_Geometry& cpu, GPU_Geometry& gpu){
    if (m>0){
        //recursion should not care about direction i dont think since the shape is symmetric around the x axis
        // We create a perpendicular unit and a parallel unit to jump convenient amounts.
        glm::vec3 parr = (d-a)/3.f; // across the top of the super-cup
        glm::vec3 perp = -glm::vec3(-parr[1],parr[0],0.f); // towards the base of the super-cup

        hilbert(a+perp,a,m-1,cpu,gpu);
        hilbert(d,d+perp,m-1,cpu,gpu);

        glm::vec3 b = a+2.f*perp;
        hilbert(b,b+parr,m-1,cpu,gpu);

        glm::vec3 c = b+2.f*parr;
        hilbert(c,c+parr,m-1,cpu,gpu);

        //TODO this is not done
    } else{
        //The base case is to draw the "cup" shape, given the coordinates at the opening
        draw_cup(a,d,cpu,gpu);
    }
}

// I accidentally made this after a mistake in the pythagoras recursion logic
void otherfractal(glm::vec3 a, glm::vec3 b, int m, CPU_Geometry& cpu, GPU_Geometry& gpu){
    if (m>0 ){
        glm::vec3 ab = b-a;
        glm::vec3 mid = (b+a)/2.f;

        glm::vec3 perp= glm::vec3(-ab[1],ab[0],0.f);

        glm::vec3 c = mid+perp/2.f;
        otherfractal(a,c,m-1,cpu,gpu);
        otherfractal(c,b,m-1,cpu,gpu);
    }
    else{
        draw_leaf(a,b,cpu,gpu);
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
        // glDisable(GL_CULL_FACE);

		glEnable(GL_FRAMEBUFFER_SRGB); // Expect Colour to be encoded in sRGB standard (as opposed to RGB) 
		// https://www.viewsonic.com/library/creative-work/srgb-vs-adobe-rgb-which-one-to-use/
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); // Clear render screen (all zero) and depth (all max depth)
        //glBufferSubData(GL_ARRAY_BUFFER,0,141,NULL);

        if (type==0){ //SIERPINSKI CASE
            divide_triangle(
                glm::vec3(-0.5f, -0.5f, 0.f),
                glm::vec3(0.5f, -0.5f, 0.f),
                glm::vec3(0.f, 0.5f, 0.f),
                depth,cpu,gpu
            );
        } 
        if (type==1){ // SPONGE CASE
            if (depth==0){
                draw_square(
                    glm::vec3(-0.5f, 0.5f, 0.f),
                    glm::vec3(0.5f, -0.5f, 0.f),
                    glm::vec3(0.5f,0,0.5f),
                    cpu,gpu
                );
            }
            else{
                divide_square(
                    glm::vec3(-0.5f, -0.5f, 0.f),
                    glm::vec3(0.5f, -1.f, 0.f),
                    depth,cpu,gpu
                );
            }
        }
        if (type==2){ //PYTHAGORAS
            pythagoras(
                glm::vec3(-0.2f, -0.8f, 0.f),
                glm::vec3(0.2f,-0.8f, 0.f),
                depth,cpu,gpu
            );
        }
        if (type==3){ //KOCH
            koch_line(
                glm::vec3(-0.5f,0.5f,0.f),
                glm::vec3(0.5f,0.5f,0.f),
                depth, cpu,gpu
            );
            koch_line(
                glm::vec3(0.f,-0.5f,0.f),
                glm::vec3(-0.5f,0.5f,0.f),
                depth, cpu,gpu
            );
            koch_line(
                glm::vec3(0.5f,0.5f,0.f),
                glm::vec3(0.f,-0.5f,0.f),
                depth, cpu,gpu
            );
        }
        if (type==4){ //DRAGON CURVE
            dragon(
                glm::vec3(-0.5f,0.f,0.f),
                glm::vec3(0.5f,0.f,0.f),
                depth,cpu,gpu
            );
        }
        if (type==5){ //HILBERT CURVE
            hilbert(
                glm::vec3(-0.5f,0.5f,0.f),
                glm::vec3(0.5f,0.5f,0.f),
                depth,cpu,gpu
            );
        }
        if (type==6){//BONUS ACCIDENT FRACTAL
            otherfractal(
                glm::vec3(-0.3f,-0.5f,0.f),
                glm::vec3(0.3f,-0.5f,0.f),
                depth,cpu,gpu
            );
        }


        gpu.setCols(cpu.cols); // Upload vertex colour attribute to VBO
        gpu.setVerts(cpu.verts); // Upload vertex position geometry to VBO
		glDisable(GL_FRAMEBUFFER_SRGB); // disable sRGB for things like imgui (if used)

		window.swapBuffers(); //Swap the buffers while displaying the previous 
	}

	glfwTerminate(); // Clean up GLFW
	return 0;
}
