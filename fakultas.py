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
        print("Fakultas",n2,"lebih tua daripada Fakultas",n1)
    elif t1 < t2:
        print("Fakultas",n1,"lebih tua daripada Fakultas",n2)
    else:
        print("Fakultas",n1,"dan",n2,"berdiri pada tahun yang sama")

def program(fakultas1, fakultas2, j_prodi1, j_prodi2):
    if j_prodi1 > j_prodi2:
        print("Fakultas",fakultas1, "memiliki lebih banyak program studi daripada Fakultas",fakultas2)
    elif j_prodi1 < j_prodi2:
        print("Fakultas",fakultas2, "memiliki lebih banyak program studi daripada Fakultas",fakultas1)
    else:
        print("Jumlah program studi Fakultas",fakultas1,"dan Fakultas",fakultas2,"sama")


def umur_fakultas(n_fakultas, t_berdiri):
    umur = 2023 - t_berdiri
    print("Fakultas",n_fakultas,"telah berumur", umur, "tahun")

env.define_function(older_faculty)
env.define_function(program)
env.define_function(umur_fakultas)

env.eval('(older_faculty "Biologi" "Filsafat" 1955 1967)')
env.eval('(older_faculty "Kehutanan" "Farmasi" 1963 1946)')
env.eval('(older_faculty "Hukum" "Ilmu Budaya" 1946 1946)')

env.eval('(program "Geografi" "Biologi" 3 3)')
env.eval('(program "Peternakan" "Ilmu Sosial dan Ilmu Politik" 4 17)')
env.eval('(program "Ekonomika dan Bisnis" "Teknologi Pertanian" 14 10)')

env.eval('(umur_fakultas "Kedokteran Hewan" 1949)')
env.eval('(umur_fakultas "Matematika dan Ilmu Pengetahuan Alam" 1955)')
env.eval('(umur_fakultas "Kedokteran, Kesehatan Masyarakat, dan Keperawatan" 1946)')
env.eval('(umur_fakultas "Filsafat" 1967)')
env.eval('(umur_fakultas "Kedokteran Gigi" 1948)')


# !! <Percobaan dengan value yang diambil dari dictionary>
# older_faculty(fakultasDict[0]['nama'], fakultasDict[1]['nama'], fakultasDict[0]['tahun'], fakultasDict[1]['tahun']) #salah?:(

# !! <Percobaan dengan sintaks 'find-fact', belum berhasil>
# env.eval('(umur_fakultas (find-fact ((?f fakultas))(eq ?f:nama "Farmasi")))')

env.run()

# env.eval('(printout t "Hello World!" crlf)')