from libcpp.vector cimport vector

cdef extern from "swalignimp.c":
	double swalignimpconstrained(double* S, int N, int M)