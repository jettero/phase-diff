#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: am modulator
# Author: Paul Miller
# Description: gnuradio flow graph
# Generated: Fri Feb 26 13:25:59 2010
##################################################

from gnuradio import gr

class am_mod(gr.top_block):

	def __init__(self):
		gr.top_block.__init__(self, "am modulator")

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 44100
		self.freq = freq = 8000

		##################################################
		# Blocks
		##################################################
		self.gr_complex_to_float_0 = gr.complex_to_float(1)
		self.gr_float_to_complex_0 = gr.float_to_complex()
		self.gr_multiply_vxx_0 = gr.multiply_vcc(1)
		self.gr_sig_source_x_0 = gr.sig_source_c(samp_rate, gr.GR_COS_WAVE, freq, 1, 0)
		self.gr_wavfile_sink_0 = gr.wavfile_sink("8k.wav", 2, samp_rate, 16)
		self.gr_wavfile_source_0 = gr.wavfile_source("orig.wav", False)

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_sig_source_x_0, 0), (self.gr_multiply_vxx_0, 0))
		self.connect((self.gr_wavfile_source_0, 0), (self.gr_float_to_complex_0, 0))
		self.connect((self.gr_float_to_complex_0, 0), (self.gr_multiply_vxx_0, 1))
		self.connect((self.gr_wavfile_source_0, 1), (self.gr_float_to_complex_0, 1))
		self.connect((self.gr_multiply_vxx_0, 0), (self.gr_complex_to_float_0, 0))
		self.connect((self.gr_complex_to_float_0, 0), (self.gr_wavfile_sink_0, 0))
		self.connect((self.gr_complex_to_float_0, 1), (self.gr_wavfile_sink_0, 1))

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.gr_sig_source_x_0.set_sampling_freq(self.samp_rate)

	def set_freq(self, freq):
		self.freq = freq
		self.gr_sig_source_x_0.set_frequency(self.freq)

if __name__ == '__main__':
	tb = am_mod()
	tb.start()
	raw_input('Press Enter to quit: ')
	tb.stop()

