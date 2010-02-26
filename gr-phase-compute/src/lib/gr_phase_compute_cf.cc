
#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gr_phase_compute_cf.h>
#include <gr_io_signature.h>
#include <gr_math.h>

#define M_TWOPI (2*M_PI)

gr_phase_compute_cf_sptr gr_make_phase_compute_cf() {
    return gr_phase_compute_cf_sptr (new gr_phase_compute_cf());
}

gr_phase_compute_cf::gr_phase_compute_cf() :
    gr_block( "phase_compute_cf", gr_make_io_signature(2,2, sizeof(gr_complex)), gr_make_io_signature(1,1, sizeof(float)) ) {
}

gr_phase_compute_cf::~gr_phase_compute_cf() {
}

float gr_phase_compute_cf::mod_2pi(float in) {

    if(in>M_PI)
        return in-M_TWOPI;

    else if(in<-M_PI)
        return in+M_TWOPI;

    return in;
}

int gr_phase_compute_cf::general_work (int noutput_items,
			       gr_vector_int &ninput_items,
			       gr_vector_const_void_star &input_items,
			       gr_vector_void_star &output_items) {

    const gr_complex *i1 = (gr_complex *) input_items[0];
    const gr_complex *i2 = (gr_complex *) input_items[1];
    float *o             = (float *) output_items[0];

    *o = mod_2pi(
        gr_fast_atan2f(i1->imag(), i1->real())
       -gr_fast_atan2f(i2->imag(), i2->real())
    );

    // Tell runtime system how many input items we consumed on
    // each input stream.
    consume_each(noutput_items);

    // Tell runtime system how many output items we produced.
    return noutput_items;
}
