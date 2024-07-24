#include "NoListaDupla.h"
#include <cstddef>

NoListaDupla::NoListaDupla(int v):
    info{ v },
    ant{ NULL },
    prox{ NULL }
{}