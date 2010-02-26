%feature("autodoc", "1");		// generate python docstrings

%include "exception.i"
%import "gnuradio.i"			// the common stuff

%{
#include "gnuradio_swig_bug_workaround.h"	// mandatory bug fix
#include "wmu_phase_compute_cf.h"
#include <stdexcept>
%}

// ----------------------------------------------------------------

/*
 * First arg is the package prefix.
 * Second arg is the name of the class minus the prefix.
 *
 * This does some behind-the-scenes magic so we can
 * access wmu_phase_compute_cf from python as wmu.phase_compute_cf
 */
GR_SWIG_BLOCK_MAGIC(wmu,phase_compute_cf);

wmu_phase_compute_cf_sptr wmu_make_phase_compute_cf();

class wmu_phase_compute_cf : public gr_block {
    private:
        wmu_phase_compute_cf();
};
