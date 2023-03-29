import clips
env = clips.Environment()

template_string = """
(deftemplate fakultas
  (slot nama (type STRING))
  (slot tahun_berdiri (type INTEGER))
  (slot jumlah_prodi (type INTEGER))
  (slot klaster (type STRING)))
"""

env.build(template_string)
template = env.find_template('fakultas')


template.assert_fact(nama='Kedokteran, Kesehatan Masyarakat, dan Keperawatan',tahun_berdiri=1946,jumlah_prodi=23, klaster='Kesehatan')
template.assert_fact(nama='Kedokteran Gigi',tahun_berdiri=1948,jumlah_prodi=3, klaster='Kesehatan')
template.assert_fact(nama='Farmasi',tahun_berdiri=1946,jumlah_prodi=6, klaster='Kesehatan')

rule1 = """
(defrule k_kesehatan
  (fakultas (nama ?nama) (klaster "Kesehatan"))
  =>
  (printout t "Fakultas " ?nama " termasuk klaster Kesehatan" crlf))
"""
env.build(rule1)

# env.assert_string('(fakultas (nama "Farmasi") (klaster "Kesehatan"))')
env.run()

# env.eval('(printout t "Hello World!" crlf)')