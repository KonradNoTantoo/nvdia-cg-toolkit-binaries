#include <cstdlib>
#include <iostream>
#include <Cg/cg.h>

bool has_error()
{
	CGerror const error = cgGetError();

	if (error != CG_NO_ERROR)
	{
		std::cerr << cgGetErrorString(error) << std::endl;
		return true;
	}

	return false;
}

int main()
{
	CGcontext context = cgCreateContext();
	if ( false == has_error() )
	{
		cgDestroyContext(context);
		if ( false == has_error() ) return EXIT_SUCCESS;
	}
	return EXIT_FAILURE;
}
