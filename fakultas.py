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

template.assert_fact(nama='Biologi',tahun_berdiri=1955,jumlah_prodi=3, klaster='Saintek')
template.assert_fact(nama='Matematika dan Ilmu Pengetahuan Alam',tahun_berdiri=1955,jumlah_prodi=16, klaster='Saintek')
template.assert_fact(nama='Geografi',tahun_berdiri=1963,jumlah_prodi=3, klaster='Saintek')
template.assert_fact(nama='Teknik',tahun_berdiri=1946,jumlah_prodi=14, klaster='Saintek')

template.assert_fact(nama='Ekonomika dan Bisnis',tahun_berdiri=1955,jumlah_prodi=14,klaster='Soshum')
template.assert_fact(nama='Filsafat',tahun_berdiri=1967,jumlah_prodi=1,klaster='Soshum')
template.assert_fact(nama='Hukum',tahun_berdiri=1946,jumlah_prodi=1,klaster='Soshum')
template.assert_fact(nama='Ilmu Budaya',tahun_berdiri=1946,jumlah_prodi=21,klaster='Soshum')
template.assert_fact(nama='Ilmu Sosial dan Ilmu Politik',tahun_berdiri=1955,jumlah_prodi=17,klaster='Soshum')

template.assert_fact(nama='Kedokteran Hewan',tahun_berdiri=1949,jumlah_prodi=1, klaster='Agro')
template.assert_fact(nama='Kehutanan',tahun_berdiri=1963,jumlah_prodi=1, klaster='Agro')
template.assert_fact(nama='Pertanian',tahun_berdiri=1946,jumlah_prodi=9, klaster='Agro')
template.assert_fact(nama='Teknologi Pertanian',tahun_berdiri=1963,jumlah_prodi=10, klaster='Agro')
template.assert_fact(nama='Peternakan',tahun_berdiri=1969,jumlah_prodi=4, klaster='Agro')

template.assert_fact(nama='Kedokteran, Kesehatan Masyarakat, dan Keperawatan',tahun_berdiri=1946,jumlah_prodi=23, klaster='Kesehatan')
template.assert_fact(nama='Kedokteran Gigi',tahun_berdiri=1948,jumlah_prodi=3, klaster='Kesehatan')
template.assert_fact(nama='Farmasi',tahun_berdiri=1946,jumlah_prodi=6, klaster='Kesehatan')

fakultasDict = []

for fact in env.facts():
    fakultasDict.append({
       "nama": fact['nama'],
       "tahun": fact['tahun_berdiri'],
       "prodi": fact['jumlah_prodi'],
       "klaster": fact['klaster']
       })


# ====== RULES ======
RULES = [ 
   """
  (defrule k_kesehatan
    (fakultas (nama ?nama) (klaster "Kesehatan"))
    =>
    (printout t "Fakultas " ?nama " termasuk klaster Kesehatan" crlf))
  """,
  """
  (defrule k_agro
    (fakultas (nama ?nama) (klaster "Agro"))
    =>
    (printout t "Fakultas " ?nama " termasuk klaster Agro" crlf))
  """,
  """
  (defrule k_saintek
    (fakultas (nama ?nama) (klaster "Saintek"))
    =>
    (printout t "Fakultas " ?nama " termasuk klaster Saintek" crlf))
  """,
  """
  (defrule k_soshum
    (fakultas (nama ?nama) (klaster "Soshum"))
    =>
    (printout t "Fakultas " ?nama " termasuk klaster Soshum" crlf))
  """
]

for rule in RULES:
   env.build(rule)

# ====== FUNCTIONS ======
def older_faculty(n1, n2, t1, t2):
    if t1 > t2:
        print(n2, " lebih tua")
    else:
        print(n1, " lebih tua")

env.define_function(older_faculty)
env.eval('(older_faculty "Kedokteran Hewan" "ASHKDAHS" 1946 1955)')

older_faculty(fakultasDict[0]['nama'], fakultasDict[1]['nama'], fakultasDict[0]['tahun'], fakultasDict[1]['tahun']) #salah?:(

env.run()

# env.eval('(printout t "Hello World!" crlf)')