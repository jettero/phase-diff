#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: PLL phase comparison
# Author: Paul Miller
# Description: gnuradio flow graph
# Generated: Fri Feb 26 17:57:53 2010
##################################################

from gnuradio import gr
from gnuradio import wmu

class pll(gr.top_block):

	def __init__(self):
		gr.top_block.__init__(self, "PLL phase comparison")

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 44100

		##################################################
		# Blocks
		##################################################
		self.gr_file_sink_0 = gr.file_sink(gr.sizeof_float*1, "phase_diffs.dat")
		self.gr_float_to_complex_0 = gr.float_to_complex()
		self.gr_float_to_complex_1 = gr.float_to_complex()
		self.gr_wavfile_source_0 = gr.wavfile_source("8k.wav", False)
		self.gr_wavfile_source_1 = gr.wavfile_source("14k", False)
		self.wmu_phase_compute_cf_0 = wmu.phase_compute_cf()

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_wavfile_source_0, 0), (self.gr_float_to_complex_0, 0))
		self.connect((self.gr_wavfile_source_0, 1), (self.gr_float_to_complex_0, 1))
		self.connect((self.gr_wavfile_source_1, 0), (self.gr_float_to_complex_1, 0))
		self.connect((self.gr_wavfile_source_1, 1), (self.gr_float_to_complex_1, 1))
		self.connect((self.gr_float_to_complex_1, 0), (self.wmu_phase_compute_cf_0, 1))
		self.connect((self.gr_float_to_complex_0, 0), (self.wmu_phase_compute_cf_0, 0))
		self.connect((self.wmu_phase_compute_cf_0, 0), (self.gr_file_sink_0, 0))

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

if __name__ == '__main__':
	tb = pll()
	tb.start()
	raw_input('Press Enter to quit: ')
	tb.stop()

