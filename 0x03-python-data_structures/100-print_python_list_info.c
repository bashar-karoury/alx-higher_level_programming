#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <sys/types.h>
#include "object.h"
#include "Python.h"
/**
 * print_python_list_info - prints some basic info about Python list
 * @p: pointer to python object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size = 0, i;

	list_size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", (Py_SIZE(p)));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < list_size; i++)
	{
		printf("Element %d: %s\n", (int)i,
				(char *)(Py_TYPE(PyList_GetItem(p, i)))->tp_name);
	}

}
