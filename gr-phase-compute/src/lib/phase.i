%feature("autodoc", "1");		// generate python docstrings

%include "exception.i"
%import "gnuradio.i"			// the common stuff

%{
#include "gnuradio_swig_bug_workaround.h"	// mandatory bug fix
#include "gr_phase_compute_cf.h"
#include <stdexcept>
%}

// ----------------------------------------------------------------

/*
 * First arg is the package prefix.
 * Second arg is the name of the class minus the prefix.
 *
 * This does some behind-the-scenes magic so we can
 * access gr_phase_compute_cf from python as gr.phase_compute_cf
 */
GR_SWIG_BLOCK_MAGIC(gr,phase_compute_cf);

gr_phase_compute_cf_sptr gr_make_phase_compute_cf();

class gr_phase_compute_cf : public gr_block {
    private:
        gr_phase_compute_cf();
};
