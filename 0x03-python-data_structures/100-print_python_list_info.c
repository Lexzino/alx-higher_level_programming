#include <Python.h>


/**
 * print_python_list_info - Prints basic  Python lists.
 * @p: A PyObject list.
 */

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int c;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (c = 0; c < size; c++)
		printf("Element %i: %s\n", cc, Py_TYPE(obj->ob_item[c])->tp_name);
}
