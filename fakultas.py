import clips
env = clips.Environment()

# ====== FACTS ======
template_string = """
(deftemplate fakultas
  (slot nama (type STRING))
  (slot tahun_berdiri (type INTEGER))
  (slot jumlah_prodi (type INTEGER))
  (slot klaster (type STRING)))
"""

env.build(template_string)
template = env.find_template('fakultas')

template.assert_fact(nama='Kedokteran Hewan',tahun_berdiri=1949,jumlah_prodi=1, klaster='Agro')
template.assert_fact(nama='Kehutanan',tahun_berdiri=1963,jumlah_prodi=1, klaster='Agro')
template.assert_fact(nama='Pertanian',tahun_berdiri=1946,jumlah_prodi=9, klaster='Agro')
template.assert_fact(nama='Teknologi Pertanian',tahun_berdiri=1963,jumlah_prodi=10, klaster='Agro')
template.assert_fact(nama='Peternakan',tahun_berdiri=1969,jumlah_prodi=4, klaster='Agro')

template.assert_fact(nama='Kedokteran, Kesehatan Masyarakat, dan Keperawatan',tahun_berdiri=1946,jumlah_prodi=23, klaster='Kesehatan')
template.assert_fact(nama='Kedokteran Gigi',tahun_berdiri=1948,jumlah_prodi=3, klaster='Kesehatan')
template.assert_fact(nama='Farmasi',tahun_berdiri=1946,jumlah_prodi=6, klaster='Kesehatan')

# print(fact1['tahun_berdiri'])
# print(type(fact1['tahun_berdiri']))

class Fakultas:
  def __init__(self, nama, tahun):
    self.nama = nama
    self.tahun = tahun

test = []

# for fact in env.facts():
#     if fact.template.name == 'fakultas':
#         test.append(fact)

# print(test)

for fact in env.facts():
    test.append({
       "nama": fact['nama'],
       "tahun": fact['tahun_berdiri']
       })

nama1 = test[0]['nama']
nama2 = test[1]['nama']
tahun1 = test[0]['tahun']
tahun2 = test[1]['tahun']

print(nama1)

# ====== RULES ======
rule1 = """
(defrule k_kesehatan
  (fakultas (nama ?nama) (klaster "Kesehatan"))
  =>
  (printout t "Fakultas " ?nama " termasuk klaster Kesehatan" crlf))
"""
env.build(rule1)

rule2 = """
(defrule k_agro
  (fakultas (nama ?nama) (klaster "Agro"))
  =>
  (printout t "Fakultas " ?nama " termasuk klaster Agro" crlf))
"""
env.build(rule2)

# ====== FUNCTIONS ======
def older_faculty(n1, n2, t1, t2):
    if t1 > t2:
        print(n2, " lebih tua")
    else:
        print(n1, " lebih tua")

env.define_function(older_faculty)
env.eval('(older_faculty "Kedokteran Hewan" "ASHKDAHS" 1946 1955)')

older_faculty(test[0]['nama'], test[1]['nama'], test[0]['tahun'], test[1]['tahun']) #salah?:(

env.run()

# env.eval('(printout t "Hello World!" crlf)')