#ifndef INCLUDED_CBC_BLOWFISH_VBB_H
#define INCLUDED_CBC_BLOWFISH_VBB_H

#include <gr_block.h>

class wmu_phase_compute_cf;

/*
 * We use boost::shared_ptr's instead of raw pointers for all access
 * to gr_blocks (and many other data structures).  The shared_ptr gets
 * us transparent reference counting, which greatly simplifies storage
 * management issues.  This is especially helpful in our hybrid
 * C++ / Python system.
 *
 * See http://www.boost.org/libs/smart_ptr/smart_ptr.htm
 *
 * As a convention, the _sptr suffix indicates a boost::shared_ptr
 */
typedef boost::shared_ptr<wmu_phase_compute_cf> wmu_phase_compute_cf_sptr;

/*!
 * \brief Return a shared_ptr to a new instance of wmu_phase_compute_cf.
 *
 * To avoid accidental use of raw pointers, wmu_phase_compute_cf's
 * constructor is private.  wmu_make_phase_compute_cf is the public
 * interface for creating new instances.
 */
wmu_phase_compute_cf_sptr wmu_make_phase_compute_cf();

/*!
 * \brief square a stream of bytes.
 * \ingroup block
 */
class wmu_phase_compute_cf : public gr_block {
    private:
        // The friend declaration allows phase_make_compute_cf to
        // access the private constructor.

        friend wmu_phase_compute_cf_sptr wmu_make_phase_compute_cf();

        float mod_2pi(float in);

        wmu_phase_compute_cf(); // private constructor

    public:
        ~wmu_phase_compute_cf(); // public destructor

        // Where all the action really happens

        int general_work (int noutput_items,
                gr_vector_int &ninput_items,
                gr_vector_const_void_star &input_items,
                gr_vector_void_star &output_items);
};

#endif
