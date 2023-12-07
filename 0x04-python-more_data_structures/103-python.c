#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <sys/types.h>
#include "object.h"
#include "listobject.h"
#include "bytesobject.h"
#include <string.h>
void print_python_bytes(PyObject *p);
/**
 * print_python_list - prints some basic info about Python list
 * @p: pointer to python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t list_size = 0, i;
	PyListObject *list_object_ptr = ((PyListObject *)p);

	list_size = list_object_ptr->ob_base.ob_size;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < list_size; i++)
	{
		printf("Element %d: %s\n",
					(int)i, (char *)(((PyObject *)
					((list_object_ptr->ob_item)[i]))->ob_type)->tp_name);
		if (strcmp((char *)(((PyObject *)
			((list_object_ptr->ob_item)[i]))->ob_type)->tp_name, "bytes") == 0)
			print_python_bytes((PyObject *)((PyObject *)
				((list_object_ptr->ob_item)[i])));
	}

}
/**
 * print_python_bytes - pirnts basic info about bytes object
 * @p: pointer to python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t  p_size = 0;
	int  i, print_size;
	PyBytesObject *bytes_object_ptr = ((PyBytesObject *)p);

	p_size = bytes_object_ptr->ob_base.ob_size;
	printf("[.] bytes object info\n");

	printf("  size: %ld\n", p_size);

	printf("  trying string: %s\n", bytes_object_ptr->ob_sval);
	print_size = (p_size < 10) ? p_size + 1 : 10;
	printf("  first %d bytes:", print_size);
	for (i = 0; i < print_size; i++)
	{
		printf(" %02x ", (unsigned char)bytes_object_ptr->ob_sval[i]);
	}
	printf("\n");
}
