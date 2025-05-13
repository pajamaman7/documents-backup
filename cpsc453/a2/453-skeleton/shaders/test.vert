#version 330 core
//layout (location = 0) in vec3 pos;
layout (location = 1) in vec2 texCoord;

// TODO is this the uniform stuff we're supposed to do??
uniform vec3 pos;
in mat4 transformationMatrix;

out vec2 tc;

void main() {
	tc = texCoord;
	gl_Position = vec4(pos, 1.0);
}
