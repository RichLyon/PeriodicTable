"""
This module contains data for all elements in the periodic table.
Each element includes basic information and electron configuration for Bohr model visualization.
"""

# Main data array containing all element information
ELEMENTS_DATA = [
  {
    "atomic_number": 1,
    "symbol": "H",
    "name": "Hydrogen",
    "atomic_mass": 1.008,
    "category": "nonmetal",
    "electron_configuration": "1s1",
    "electron_shells": [1],
    "description": "Hydrogen is the lightest element and the most abundant chemical substance in the universe."
  },
  {
    "atomic_number": 2,
    "symbol": "He",
    "name": "Helium",
    "atomic_mass": 4.003,
    "category": "noble gas",
    "electron_configuration": "1s2",
    "electron_shells": [2],
    "description": "Helium is a colorless, odorless noble gas, the second most abundant element in the universe."
  },
  {
    "atomic_number": 3,
    "symbol": "Li",
    "name": "Lithium",
    "atomic_mass": 6.94,
    "category": "alkali metal",
    "electron_configuration": "[He] 2s1",
    "electron_shells": [2, 1],
    "description": "Lithium is a soft, silvery-white metal, the lightest of the alkali metals."
  },
  {
    "atomic_number": 4,
    "symbol": "Be",
    "name": "Beryllium",
    "atomic_mass": 9.012,
    "category": "alkaline earth metal",
    "electron_configuration": "[He] 2s2",
    "electron_shells": [2, 2],
    "description": "Beryllium is a hard, gray metal that is relatively rare and highly toxic in powdered form."
  },
  {
    "atomic_number": 5,
    "symbol": "B",
    "name": "Boron",
    "atomic_mass": 10.81,
    "category": "metalloid",
    "electron_configuration": "[He] 2s2 2p1",
    "electron_shells": [2, 3],
    "description": "Boron is a metalloid essential for plant growth and found in borate minerals."
  },
  {
    "atomic_number": 6,
    "symbol": "C",
    "name": "Carbon",
    "atomic_mass": 12.011,
    "category": "nonmetal",
    "electron_configuration": "[He] 2s2 2p2",
    "electron_shells": [2, 4],
    "description": "Carbon is a nonmetal that forms the basis for all known life on Earth."
  },
  {
    "atomic_number": 7,
    "symbol": "N",
    "name": "Nitrogen",
    "atomic_mass": 14.007,
    "category": "nonmetal",
    "electron_configuration": "[He] 2s2 2p3",
    "electron_shells": [2, 5],
    "description": "Nitrogen is a colorless, odorless gas making up around 78% of Earth’s atmosphere."
  },
  {
    "atomic_number": 8,
    "symbol": "O",
    "name": "Oxygen",
    "atomic_mass": 15.999,
    "category": "nonmetal",
    "electron_configuration": "[He] 2s2 2p4",
    "electron_shells": [2, 6],
    "description": "Oxygen is a highly reactive nonmetal that is essential for most life forms on Earth."
  },
  {
    "atomic_number": 9,
    "symbol": "F",
    "name": "Fluorine",
    "atomic_mass": 18.998,
    "category": "halogen",
    "electron_configuration": "[He] 2s2 2p5",
    "electron_shells": [2, 7],
    "description": "Fluorine is the most reactive and electronegative element, a pale yellow gas at room temperature."
  },
  {
    "atomic_number": 10,
    "symbol": "Ne",
    "name": "Neon",
    "atomic_mass": 20.180,
    "category": "noble gas",
    "electron_configuration": "[He] 2s2 2p6",
    "electron_shells": [2, 8],
    "description": "Neon is a noble gas used in lighting and known for its distinct reddish-orange glow."
  },
  {
    "atomic_number": 11,
    "symbol": "Na",
    "name": "Sodium",
    "atomic_mass": 22.990,
    "category": "alkali metal",
    "electron_configuration": "[Ne] 3s1",
    "electron_shells": [2, 8, 1],
    "description": "Sodium is a highly reactive, soft metal essential in many biological processes."
  },
  {
    "atomic_number": 12,
    "symbol": "Mg",
    "name": "Magnesium",
    "atomic_mass": 24.305,
    "category": "alkaline earth metal",
    "electron_configuration": "[Ne] 3s2",
    "electron_shells": [2, 8, 2],
    "description": "Magnesium is a shiny gray metal that burns with a bright white flame."
  },
  {
    "atomic_number": 13,
    "symbol": "Al",
    "name": "Aluminium",
    "atomic_mass": 26.982,
    "category": "post-transition metal",
    "electron_configuration": "[Ne] 3s2 3p1",
    "electron_shells": [2, 8, 3],
    "description": "Aluminium is a silvery-white, lightweight metal used in a wide range of applications."
  },
  {
    "atomic_number": 14,
    "symbol": "Si",
    "name": "Silicon",
    "atomic_mass": 28.085,
    "category": "metalloid",
    "electron_configuration": "[Ne] 3s2 3p2",
    "electron_shells": [2, 8, 4],
    "description": "Silicon is a metalloid widely used in semiconductors and computer chips."
  },
  {
    "atomic_number": 15,
    "symbol": "P",
    "name": "Phosphorus",
    "atomic_mass": 30.974,
    "category": "nonmetal",
    "electron_configuration": "[Ne] 3s2 3p3",
    "electron_shells": [2, 8, 5],
    "description": "Phosphorus is a highly reactive nonmetal essential in biology, found in DNA and ATP."
  },
  {
    "atomic_number": 16,
    "symbol": "S",
    "name": "Sulfur",
    "atomic_mass": 32.06,
    "category": "nonmetal",
    "electron_configuration": "[Ne] 3s2 3p4",
    "electron_shells": [2, 8, 6],
    "description": "Sulfur is a bright yellow, brittle nonmetal used in fertilizers and gunpowder."
  },
  {
    "atomic_number": 17,
    "symbol": "Cl",
    "name": "Chlorine",
    "atomic_mass": 35.45,
    "category": "halogen",
    "electron_configuration": "[Ne] 3s2 3p5",
    "electron_shells": [2, 8, 7],
    "description": "Chlorine is a yellow-green gas used widely as a disinfectant and in PVC plastic production."
  },
  {
    "atomic_number": 18,
    "symbol": "Ar",
    "name": "Argon",
    "atomic_mass": 39.948,
    "category": "noble gas",
    "electron_configuration": "[Ne] 3s2 3p6",
    "electron_shells": [2, 8, 8],
    "description": "Argon is a colorless, odorless noble gas used in lighting and welding."
  },
  {
    "atomic_number": 19,
    "symbol": "K",
    "name": "Potassium",
    "atomic_mass": 39.098,
    "category": "alkali metal",
    "electron_configuration": "[Ar] 4s1",
    "electron_shells": [2, 8, 8, 1],
    "description": "Potassium is a soft, reactive metal essential for living cells and electrolytes."
  },
  {
    "atomic_number": 20,
    "symbol": "Ca",
    "name": "Calcium",
    "atomic_mass": 40.078,
    "category": "alkaline earth metal",
    "electron_configuration": "[Ar] 4s2",
    "electron_shells": [2, 8, 8, 2],
    "description": "Calcium is a silvery-gray metal important for bones and teeth in living organisms."
  },
  {
    "atomic_number": 21,
    "symbol": "Sc",
    "name": "Scandium",
    "atomic_mass": 44.956,
    "category": "transition metal",
    "electron_configuration": "[Ar] 3d1 4s2",
    "electron_shells": [2, 8, 9, 2],
    "description": "Scandium is a soft, silvery transition metal sometimes used in alloys."
  },
  {
    "atomic_number": 22,
    "symbol": "Ti",
    "name": "Titanium",
    "atomic_mass": 47.867,
    "category": "transition metal",
    "electron_configuration": "[Ar] 3d2 4s2",
    "electron_shells": [2, 8, 10, 2],
    "description": "Titanium is a strong, lightweight metal resistant to corrosion, widely used in aerospace."
  },
  {
    "atomic_number": 23,
    "symbol": "V",
    "name": "Vanadium",
    "atomic_mass": 50.942,
    "category": "transition metal",
    "electron_configuration": "[Ar] 3d3 4s2",
    "electron_shells": [2, 8, 11, 2],
    "description": "Vanadium is a hard, silvery-gray metal used to strengthen steel alloys."
  },
  {
    "atomic_number": 24,
    "symbol": "Cr",
    "name": "Chromium",
    "atomic_mass": 52.0,
    "category": "transition metal",
    "electron_configuration": "[Ar] 3d5 4s1",
    "electron_shells": [2, 8, 13, 1],
    "description": "Chromium is a lustrous, hard metal known for its high polish and corrosion resistance."
  },
  {
    "atomic_number": 25,
    "symbol": "Mn",
    "name": "Manganese",
    "atomic_mass": 54.938,
    "category": "transition metal",
    "electron_configuration": "[Ar] 3d5 4s2",
    "electron_shells": [2, 8, 13, 2],
    "description": "Manganese is a metal used to form important alloys such as stainless steel."
  },
  {
    "atomic_number": 26,
    "symbol": "Fe",
    "name": "Iron",
    "atomic_mass": 55.845,
    "category": "transition metal",
    "electron_configuration": "[Ar] 3d6 4s2",
    "electron_shells": [2, 8, 14, 2],
    "description": "Iron is a crucial metal for construction and is the main component of steel."
  },
  {
    "atomic_number": 27,
    "symbol": "Co",
    "name": "Cobalt",
    "atomic_mass": 58.933,
    "category": "transition metal",
    "electron_configuration": "[Ar] 3d7 4s2",
    "electron_shells": [2, 8, 15, 2],
    "description": "Cobalt is a lustrous, silvery-blue metal used in alloys and rechargeable batteries."
  },
  {
    "atomic_number": 28,
    "symbol": "Ni",
    "name": "Nickel",
    "atomic_mass": 58.693,
    "category": "transition metal",
    "electron_configuration": "[Ar] 3d8 4s2",
    "electron_shells": [2, 8, 16, 2],
    "description": "Nickel is a silvery-white metal resistant to corrosion, often used in alloys."
  },
  {
    "atomic_number": 29,
    "symbol": "Cu",
    "name": "Copper",
    "atomic_mass": 63.546,
    "category": "transition metal",
    "electron_configuration": "[Ar] 3d10 4s1",
    "electron_shells": [2, 8, 18, 1],
    "description": "Copper is a reddish metal with high electrical conductivity, used in wiring."
  },
  {
    "atomic_number": 30,
    "symbol": "Zn",
    "name": "Zinc",
    "atomic_mass": 65.38,
    "category": "transition metal",
    "electron_configuration": "[Ar] 3d10 4s2",
    "electron_shells": [2, 8, 18, 2],
    "description": "Zinc is a bluish-silver metal used to galvanize steel and in die-casting alloys."
  },
  {
    "atomic_number": 31,
    "symbol": "Ga",
    "name": "Gallium",
    "atomic_mass": 69.723,
    "category": "post-transition metal",
    "electron_configuration": "[Ar] 3d10 4s2 4p1",
    "electron_shells": [2, 8, 18, 3],
    "description": "Gallium is a soft, silvery metal that melts near room temperature."
  },
  {
    "atomic_number": 32,
    "symbol": "Ge",
    "name": "Germanium",
    "atomic_mass": 72.63,
    "category": "metalloid",
    "electron_configuration": "[Ar] 3d10 4s2 4p2",
    "electron_shells": [2, 8, 18, 4],
    "description": "Germanium is a metalloid important for semiconductor applications."
  },
  {
    "atomic_number": 33,
    "symbol": "As",
    "name": "Arsenic",
    "atomic_mass": 74.922,
    "category": "metalloid",
    "electron_configuration": "[Ar] 3d10 4s2 4p3",
    "electron_shells": [2, 8, 18, 5],
    "description": "Arsenic is a metalloid known for its toxicity and use in pesticides."
  },
  {
    "atomic_number": 34,
    "symbol": "Se",
    "name": "Selenium",
    "atomic_mass": 78.971,
    "category": "nonmetal",
    "electron_configuration": "[Ar] 3d10 4s2 4p4",
    "electron_shells": [2, 8, 18, 6],
    "description": "Selenium is a nonmetal with properties similar to sulfur, used in electronics and glassmaking."
  },
  {
    "atomic_number": 35,
    "symbol": "Br",
    "name": "Bromine",
    "atomic_mass": 79.904,
    "category": "halogen",
    "electron_configuration": "[Ar] 3d10 4s2 4p5",
    "electron_shells": [2, 8, 18, 7],
    "description": "Bromine is a reddish-brown liquid at room temperature, the only nonmetallic element that is liquid."
  },
  {
    "atomic_number": 36,
    "symbol": "Kr",
    "name": "Krypton",
    "atomic_mass": 83.798,
    "category": "noble gas",
    "electron_configuration": "[Ar] 3d10 4s2 4p6",
    "electron_shells": [2, 8, 18, 8],
    "description": "Krypton is a colorless, odorless noble gas used in lighting and photography."
  },
  {
    "atomic_number": 37,
    "symbol": "Rb",
    "name": "Rubidium",
    "atomic_mass": 85.468,
    "category": "alkali metal",
    "electron_configuration": "[Kr] 5s1",
    "electron_shells": [2, 8, 18, 8, 1],
    "description": "Rubidium is a highly reactive alkali metal that ignites spontaneously in air."
  },
  {
    "atomic_number": 38,
    "symbol": "Sr",
    "name": "Strontium",
    "atomic_mass": 87.62,
    "category": "alkaline earth metal",
    "electron_configuration": "[Kr] 5s2",
    "electron_shells": [2, 8, 18, 8, 2],
    "description": "Strontium is a soft, silvery metal that burns with a bright red flame."
  },
  {
    "atomic_number": 39,
    "symbol": "Y",
    "name": "Yttrium",
    "atomic_mass": 88.906,
    "category": "transition metal",
    "electron_configuration": "[Kr] 4d1 5s2",
    "electron_shells": [2, 8, 18, 9, 2],
    "description": "Yttrium is a silvery-metallic transition metal used in LEDs and phosphors."
  },
  {
    "atomic_number": 40,
    "symbol": "Zr",
    "name": "Zirconium",
    "atomic_mass": 91.224,
    "category": "transition metal",
    "electron_configuration": "[Kr] 4d2 5s2",
    "electron_shells": [2, 8, 18, 10, 2],
    "description": "Zirconium is a lustrous, grey-white metal resistant to corrosion, often used in nuclear reactors."
  },
  {
    "atomic_number": 41,
    "symbol": "Nb",
    "name": "Niobium",
    "atomic_mass": 92.906,
    "category": "transition metal",
    "electron_configuration": "[Kr] 4d4 5s1",
    "electron_shells": [2, 8, 18, 12, 1],
    "description": "Niobium is a soft, gray transition metal used in superconducting alloys."
  },
  {
    "atomic_number": 42,
    "symbol": "Mo",
    "name": "Molybdenum",
    "atomic_mass": 95.95,
    "category": "transition metal",
    "electron_configuration": "[Kr] 4d5 5s1",
    "electron_shells": [2, 8, 18, 13, 1],
    "description": "Molybdenum is a hard, silvery metal with a high melting point, used to strengthen steel."
  },
  {
    "atomic_number": 43,
    "symbol": "Tc",
    "name": "Technetium",
    "atomic_mass": 98,
    "category": "transition metal",
    "electron_configuration": "[Kr] 4d5 5s2",
    "electron_shells": [2, 8, 18, 13, 2],
    "description": "Technetium is the lightest element with no stable isotopes, used in medical imaging."
  },
  {
    "atomic_number": 44,
    "symbol": "Ru",
    "name": "Ruthenium",
    "atomic_mass": 101.07,
    "category": "transition metal",
    "electron_configuration": "[Kr] 4d7 5s1",
    "electron_shells": [2, 8, 18, 15, 1],
    "description": "Ruthenium is a rare transition metal used in electronics and chemical catalysts."
  },
  {
    "atomic_number": 45,
    "symbol": "Rh",
    "name": "Rhodium",
    "atomic_mass": 102.905,
    "category": "transition metal",
    "electron_configuration": "[Kr] 4d8 5s1",
    "electron_shells": [2, 8, 18, 16, 1],
    "description": "Rhodium is a rare, silvery-white, corrosion-resistant metal used in catalytic converters."
  },
  {
    "atomic_number": 46,
    "symbol": "Pd",
    "name": "Palladium",
    "atomic_mass": 106.42,
    "category": "transition metal",
    "electron_configuration": "[Kr] 4d10",
    "electron_shells": [2, 8, 18, 18],
    "description": "Palladium is a shiny, silvery-white metal used in catalytic converters and electronics."
  },
  {
    "atomic_number": 47,
    "symbol": "Ag",
    "name": "Silver",
    "atomic_mass": 107.868,
    "category": "transition metal",
    "electron_configuration": "[Kr] 4d10 5s1",
    "electron_shells": [2, 8, 18, 18, 1],
    "description": "Silver is a precious metal with the highest electrical and thermal conductivity of all metals."
  },
  {
    "atomic_number": 48,
    "symbol": "Cd",
    "name": "Cadmium",
    "atomic_mass": 112.414,
    "category": "transition metal",
    "electron_configuration": "[Kr] 4d10 5s2",
    "electron_shells": [2, 8, 18, 18, 2],
    "description": "Cadmium is a bluish-white metal used in batteries but is highly toxic."
  },
  {
    "atomic_number": 49,
    "symbol": "In",
    "name": "Indium",
    "atomic_mass": 114.818,
    "category": "post-transition metal",
    "electron_configuration": "[Kr] 4d10 5s2 5p1",
    "electron_shells": [2, 8, 18, 18, 3],
    "description": "Indium is a soft, silvery metal that is easily fusible and used in LCDs."
  },
  {
    "atomic_number": 50,
    "symbol": "Sn",
    "name": "Tin",
    "atomic_mass": 118.71,
    "category": "post-transition metal",
    "electron_configuration": "[Kr] 4d10 5s2 5p2",
    "electron_shells": [2, 8, 18, 18, 4],
    "description": "Tin is a soft, silvery metal used to coat other metals to prevent corrosion."
  },
  {
    "atomic_number": 51,
    "symbol": "Sb",
    "name": "Antimony",
    "atomic_mass": 121.76,
    "category": "metalloid",
    "electron_configuration": "[Kr] 4d10 5s2 5p3",
    "electron_shells": [2, 8, 18, 18, 5],
    "description": "Antimony is a brittle metalloid used in alloys for batteries, bullets, and flame retardants."
  },
  {
    "atomic_number": 52,
    "symbol": "Te",
    "name": "Tellurium",
    "atomic_mass": 127.6,
    "category": "metalloid",
    "electron_configuration": "[Kr] 4d10 5s2 5p4",
    "electron_shells": [2, 8, 18, 18, 6],
    "description": "Tellurium is a metalloid used in alloys to improve machinability and in semiconductor technology."
  },
  {
    "atomic_number": 53,
    "symbol": "I",
    "name": "Iodine",
    "atomic_mass": 126.904,
    "category": "halogen",
    "electron_configuration": "[Kr] 4d10 5s2 5p5",
    "electron_shells": [2, 8, 18, 18, 7],
    "description": "Iodine is a violet-colored solid halogen essential in trace amounts for living organisms."
  },
  {
    "atomic_number": 54,
    "symbol": "Xe",
    "name": "Xenon",
    "atomic_mass": 131.293,
    "category": "noble gas",
    "electron_configuration": "[Kr] 4d10 5s2 5p6",
    "electron_shells": [2, 8, 18, 18, 8],
    "description": "Xenon is a colorless, dense noble gas used in high-intensity lamps and anesthesia."
  },
  {
    "atomic_number": 55,
    "symbol": "Cs",
    "name": "Cesium",
    "atomic_mass": 132.905,
    "category": "alkali metal",
    "electron_configuration": "[Xe] 6s1",
    "electron_shells": [2, 8, 18, 18, 8, 1],
    "description": "Cesium is an extremely reactive alkali metal, the most electropositive of all stable elements."
  },
  {
    "atomic_number": 56,
    "symbol": "Ba",
    "name": "Barium",
    "atomic_mass": 137.327,
    "category": "alkaline earth metal",
    "electron_configuration": "[Xe] 6s2",
    "electron_shells": [2, 8, 18, 18, 8, 2],
    "description": "Barium is a soft, silvery alkaline earth metal used in drilling fluids and fireworks."
  },
  {
    "atomic_number": 57,
    "symbol": "La",
    "name": "Lanthanum",
    "atomic_mass": 138.905,
    "category": "lanthanide",
    "electron_configuration": "[Xe] 5d1 6s2",
    "electron_shells": [2, 8, 18, 18, 9, 2],
    "description": "Lanthanum is a soft, ductile metal, the first element of the lanthanide series."
  },
  {
    "atomic_number": 58,
    "symbol": "Ce",
    "name": "Cerium",
    "atomic_mass": 140.116,
    "category": "lanthanide",
    "electron_configuration": "[Xe] 4f1 5d1 6s2",
    "electron_shells": [2, 8, 18, 19, 9, 2],
    "description": "Cerium is a malleable, silvery metal used in catalytic converters and glass polishing."
  },
  {
    "atomic_number": 59,
    "symbol": "Pr",
    "name": "Praseodymium",
    "atomic_mass": 140.908,
    "category": "lanthanide",
    "electron_configuration": "[Xe] 4f3 6s2",
    "electron_shells": [2, 8, 18, 20, 9, 2],
    "description": "Praseodymium is a soft, silvery metal used in magnets, lasers, and glass coloring."
  },
  {
    "atomic_number": 60,
    "symbol": "Nd",
    "name": "Neodymium",
    "atomic_mass": 144.242,
    "category": "lanthanide",
    "electron_configuration": "[Xe] 4f4 6s2",
    "electron_shells": [2, 8, 18, 22, 8, 2],
    "description": "Neodymium is a lustrous, silvery metal primarily used in high-strength permanent magnets."
  },
  {
    "atomic_number": 61,
    "symbol": "Pm",
    "name": "Promethium",
    "atomic_mass": 145,
    "category": "lanthanide",
    "electron_configuration": "[Xe] 4f5 6s2",
    "electron_shells": [2, 8, 18, 23, 8, 2],
    "description": "Promethium is a radioactive lanthanide with no stable isotopes, used in some nuclear batteries."
  },
  {
    "atomic_number": 62,
    "symbol": "Sm",
    "name": "Samarium",
    "atomic_mass": 150.36,
    "category": "lanthanide",
    "electron_configuration": "[Xe] 4f6 6s2",
    "electron_shells": [2, 8, 18, 24, 8, 2],
    "description": "Samarium is a silvery metal used in special magnets and in certain nuclear reactor applications."
  },
  {
    "atomic_number": 63,
    "symbol": "Eu",
    "name": "Europium",
    "atomic_mass": 151.964,
    "category": "lanthanide",
    "electron_configuration": "[Xe] 4f7 6s2",
    "electron_shells": [2, 8, 18, 25, 8, 2],
    "description": "Europium is a reactive, soft metal used in phosphors for TV and computer screens."
  },
  {
    "atomic_number": 64,
    "symbol": "Gd",
    "name": "Gadolinium",
    "atomic_mass": 157.25,
    "category": "lanthanide",
    "electron_configuration": "[Xe] 4f7 5d1 6s2",
    "electron_shells": [2, 8, 18, 25, 9, 2],
    "description": "Gadolinium is a silvery-white metal used in MRI contrast agents and nuclear reactors."
  },
  {
    "atomic_number": 65,
    "symbol": "Tb",
    "name": "Terbium",
    "atomic_mass": 158.925,
    "category": "lanthanide",
    "electron_configuration": "[Xe] 4f9 6s2",
    "electron_shells": [2, 8, 18, 27, 8, 2],
    "description": "Terbium is a silvery-white, rare earth metal used in solid-state devices and green phosphors."
  },
  {
    "atomic_number": 66,
    "symbol": "Dy",
    "name": "Dysprosium",
    "atomic_mass": 162.5,
    "category": "lanthanide",
    "electron_configuration": "[Xe] 4f10 6s2",
    "electron_shells": [2, 8, 18, 28, 8, 2],
    "description": "Dysprosium is a highly magnetic rare earth metal used in magnets and nuclear reactor control rods."
  },
  {
    "atomic_number": 67,
    "symbol": "Ho",
    "name": "Holmium",
    "atomic_mass": 164.93,
    "category": "lanthanide",
    "electron_configuration": "[Xe] 4f11 6s2",
    "electron_shells": [2, 8, 18, 29, 8, 2],
    "description": "Holmium is a soft, silvery metal with the highest magnetic strength of any element."
  },
  {
    "atomic_number": 68,
    "symbol": "Er",
    "name": "Erbium",
    "atomic_mass": 167.259,
    "category": "lanthanide",
    "electron_configuration": "[Xe] 4f12 6s2",
    "electron_shells": [2, 8, 18, 30, 8, 2],
    "description": "Erbium is a silvery metal used in optical fibers and nuclear technology."
  },
  {
    "atomic_number": 69,
    "symbol": "Tm",
    "name": "Thulium",
    "atomic_mass": 168.934,
    "category": "lanthanide",
    "electron_configuration": "[Xe] 4f13 6s2",
    "electron_shells": [2, 8, 18, 31, 8, 2],
    "description": "Thulium is the second least abundant lanthanide, used in X-ray devices."
  },
  {
    "atomic_number": 70,
    "symbol": "Yb",
    "name": "Ytterbium",
    "atomic_mass": 173.045,
    "category": "lanthanide",
    "electron_configuration": "[Xe] 4f14 6s2",
    "electron_shells": [2, 8, 18, 32, 8, 2],
    "description": "Ytterbium is a soft, ductile metal used in some laser and steel alloy applications."
  },
  {
    "atomic_number": 71,
    "symbol": "Lu",
    "name": "Lutetium",
    "atomic_mass": 174.967,
    "category": "lanthanide",
    "electron_configuration": "[Xe] 4f14 5d1 6s2",
    "electron_shells": [2, 8, 18, 32, 9, 2],
    "description": "Lutetium is the last element of the lanthanide series, used in PET scan detectors."
  },
  {
    "atomic_number": 72,
    "symbol": "Hf",
    "name": "Hafnium",
    "atomic_mass": 178.49,
    "category": "transition metal",
    "electron_configuration": "[Xe] 4f14 5d2 6s2",
    "electron_shells": [2, 8, 18, 32, 10, 2],
    "description": "Hafnium is a ductile metal with high melting point, used in nuclear control rods."
  },
  {
    "atomic_number": 73,
    "symbol": "Ta",
    "name": "Tantalum",
    "atomic_mass": 180.948,
    "category": "transition metal",
    "electron_configuration": "[Xe] 4f14 5d3 6s2",
    "electron_shells": [2, 8, 18, 32, 11, 2],
    "description": "Tantalum is a hard, blue-gray metal highly resistant to corrosion, used in electronics."
  },
  {
    "atomic_number": 74,
    "symbol": "W",
    "name": "Tungsten",
    "atomic_mass": 183.84,
    "category": "transition metal",
    "electron_configuration": "[Xe] 4f14 5d4 6s2",
    "electron_shells": [2, 8, 18, 32, 12, 2],
    "description": "Tungsten is a dense metal with the highest melting point of all metallic elements."
  },
  {
    "atomic_number": 75,
    "symbol": "Re",
    "name": "Rhenium",
    "atomic_mass": 186.207,
    "category": "transition metal",
    "electron_configuration": "[Xe] 4f14 5d5 6s2",
    "electron_shells": [2, 8, 18, 32, 13, 2],
    "description": "Rhenium is a rare, silvery-white metal with very high melting point, used in alloys for jet engines."
  },
  {
    "atomic_number": 76,
    "symbol": "Os",
    "name": "Osmium",
    "atomic_mass": 190.23,
    "category": "transition metal",
    "electron_configuration": "[Xe] 4f14 5d6 6s2",
    "electron_shells": [2, 8, 18, 32, 14, 2],
    "description": "Osmium is a hard, brittle metal with the highest density of all elements."
  },
  {
    "atomic_number": 77,
    "symbol": "Ir",
    "name": "Iridium",
    "atomic_mass": 192.217,
    "category": "transition metal",
    "electron_configuration": "[Xe] 4f14 5d7 6s2",
    "electron_shells": [2, 8, 18, 32, 15, 2],
    "description": "Iridium is a very hard, brittle metal that is extremely resistant to corrosion."
  },
  {
    "atomic_number": 78,
    "symbol": "Pt",
    "name": "Platinum",
    "atomic_mass": 195.084,
    "category": "transition metal",
    "electron_configuration": "[Xe] 4f14 5d9 6s1",
    "electron_shells": [2, 8, 18, 32, 17, 1],
    "description": "Platinum is a dense, malleable metal widely used in jewelry, catalytic converters, and electronics."
  },
  {
    "atomic_number": 79,
    "symbol": "Au",
    "name": "Gold",
    "atomic_mass": 196.967,
    "category": "transition metal",
    "electron_configuration": "[Xe] 4f14 5d10 6s1",
    "electron_shells": [2, 8, 18, 32, 18, 1],
    "description": "Gold is a highly valued precious metal known for its malleability and conductivity."
  },
  {
    "atomic_number": 80,
    "symbol": "Hg",
    "name": "Mercury",
    "atomic_mass": 200.592,
    "category": "transition metal",
    "electron_configuration": "[Xe] 4f14 5d10 6s2",
    "electron_shells": [2, 8, 18, 32, 18, 2],
    "description": "Mercury is the only metallic element that is liquid at room temperature, used in thermometers."
  },
  {
    "atomic_number": 81,
    "symbol": "Tl",
    "name": "Thallium",
    "atomic_mass": 204.38,
    "category": "post-transition metal",
    "electron_configuration": "[Xe] 4f14 5d10 6s2 6p1",
    "electron_shells": [2, 8, 18, 32, 18, 3],
    "description": "Thallium is a soft, gray post-transition metal that is highly toxic."
  },
  {
    "atomic_number": 82,
    "symbol": "Pb",
    "name": "Lead",
    "atomic_mass": 207.2,
    "category": "post-transition metal",
    "electron_configuration": "[Xe] 4f14 5d10 6s2 6p2",
    "electron_shells": [2, 8, 18, 32, 18, 4],
    "description": "Lead is a soft, dense metal with a low melting point, historically used in pipes and paints."
  },
  {
    "atomic_number": 83,
    "symbol": "Bi",
    "name": "Bismuth",
    "atomic_mass": 208.98,
    "category": "post-transition metal",
    "electron_configuration": "[Xe] 4f14 5d10 6s2 6p3",
    "electron_shells": [2, 8, 18, 32, 18, 5],
    "description": "Bismuth is a brittle, crystalline, post-transition metal with a low toxicity relative to its neighbors."
  },
  {
    "atomic_number": 84,
    "symbol": "Po",
    "name": "Polonium",
    "atomic_mass": 209,
    "category": "post-transition metal",
    "electron_configuration": "[Xe] 4f14 5d10 6s2 6p4",
    "electron_shells": [2, 8, 18, 32, 18, 6],
    "description": "Polonium is a rare, highly radioactive metal discovered by Marie Curie."
  },
  {
    "atomic_number": 85,
    "symbol": "At",
    "name": "Astatine",
    "atomic_mass": 210,
    "category": "halogen",
    "electron_configuration": "[Xe] 4f14 5d10 6s2 6p5",
    "electron_shells": [2, 8, 18, 32, 18, 7],
    "description": "Astatine is a rare, radioactive halogen, the heaviest of the halogen group."
  },
  {
    "atomic_number": 86,
    "symbol": "Rn",
    "name": "Radon",
    "atomic_mass": 222,
    "category": "noble gas",
    "electron_configuration": "[Xe] 4f14 5d10 6s2 6p6",
    "electron_shells": [2, 8, 18, 32, 18, 8],
    "description": "Radon is a radioactive noble gas that can accumulate in buildings and is a health hazard."
  },
  {
    "atomic_number": 87,
    "symbol": "Fr",
    "name": "Francium",
    "atomic_mass": 223,
    "category": "alkali metal",
    "electron_configuration": "[Rn] 7s1",
    "electron_shells": [2, 8, 18, 32, 18, 8, 1],
    "description": "Francium is an extremely radioactive and reactive alkali metal, the second rarest element."
  },
  {
    "atomic_number": 88,
    "symbol": "Ra",
    "name": "Radium",
    "atomic_mass": 226,
    "category": "alkaline earth metal",
    "electron_configuration": "[Rn] 7s2",
    "electron_shells": [2, 8, 18, 32, 18, 8, 2],
    "description": "Radium is a highly radioactive, luminous alkaline earth metal used in old self-luminous paints."
  },
  {
    "atomic_number": 89,
    "symbol": "Ac",
    "name": "Actinium",
    "atomic_mass": 227,
    "category": "actinide",
    "electron_configuration": "[Rn] 6d1 7s2",
    "electron_shells": [2, 8, 18, 32, 18, 9, 2],
    "description": "Actinium is a soft, silvery radioactive metal that glows in the dark due to its radioactivity."
  },
  {
    "atomic_number": 90,
    "symbol": "Th",
    "name": "Thorium",
    "atomic_mass": 232.038,
    "category": "actinide",
    "electron_configuration": "[Rn] 6d2 7s2",
    "electron_shells": [2, 8, 18, 32, 18, 10, 2],
    "description": "Thorium is a weakly radioactive metal that can be used as nuclear fuel."
  },
  {
    "atomic_number": 91,
    "symbol": "Pa",
    "name": "Protactinium",
    "atomic_mass": 231.036,
    "category": "actinide",
    "electron_configuration": "[Rn] 5f2 6d1 7s2",
    "electron_shells": [2, 8, 18, 32, 20, 9, 2],
    "description": "Protactinium is a dense, silvery-gray actinide metal that is highly radioactive and toxic."
  },
  {
    "atomic_number": 92,
    "symbol": "U",
    "name": "Uranium",
    "atomic_mass": 238.029,
    "category": "actinide",
    "electron_configuration": "[Rn] 5f3 6d1 7s2",
    "electron_shells": [2, 8, 18, 32, 21, 9, 2],
    "description": "Uranium is a heavy, silvery metal used as a fuel in nuclear power and weapons."
  },
  {
    "atomic_number": 93,
    "symbol": "Np",
    "name": "Neptunium",
    "atomic_mass": 237,
    "category": "actinide",
    "electron_configuration": "[Rn] 5f4 6d1 7s2",
    "electron_shells": [2, 8, 18, 32, 22, 9, 2],
    "description": "Neptunium is a radioactive actinide metal produced in nuclear reactors as a byproduct."
  },
  {
    "atomic_number": 94,
    "symbol": "Pu",
    "name": "Plutonium",
    "atomic_mass": 244,
    "category": "actinide",
    "electron_configuration": "[Rn] 5f6 7s2",
    "electron_shells": [2, 8, 18, 32, 24, 8, 2],
    "description": "Plutonium is a highly radioactive metal used in nuclear weapons and reactors."
  },
  {
    "atomic_number": 95,
    "symbol": "Am",
    "name": "Americium",
    "atomic_mass": 243,
    "category": "actinide",
    "electron_configuration": "[Rn] 5f7 7s2",
    "electron_shells": [2, 8, 18, 32, 25, 8, 2],
    "description": "Americium is a synthetic radioactive metal used in smoke detectors and neutron sources."
  },
  {
    "atomic_number": 96,
    "symbol": "Cm",
    "name": "Curium",
    "atomic_mass": 247,
    "category": "actinide",
    "electron_configuration": "[Rn] 5f7 6d1 7s2",
    "electron_shells": [2, 8, 18, 32, 25, 9, 2],
    "description": "Curium is a hard, dense radioactive metal used in alpha particle research and space missions."
  },
  {
    "atomic_number": 97,
    "symbol": "Bk",
    "name": "Berkelium",
    "atomic_mass": 247,
    "category": "actinide",
    "electron_configuration": "[Rn] 5f9 7s2",
    "electron_shells": [2, 8, 18, 32, 27, 8, 2],
    "description": "Berkelium is a synthetic, radioactive element first synthesized at UC Berkeley."
  },
  {
    "atomic_number": 98,
    "symbol": "Cf",
    "name": "Californium",
    "atomic_mass": 251,
    "category": "actinide",
    "electron_configuration": "[Rn] 5f10 7s2",
    "electron_shells": [2, 8, 18, 32, 28, 8, 2],
    "description": "Californium is a highly radioactive metal used as a neutron source for various purposes."
  },
  {
    "atomic_number": 99,
    "symbol": "Es",
    "name": "Einsteinium",
    "atomic_mass": 252,
    "category": "actinide",
    "electron_configuration": "[Rn] 5f11 7s2",
    "electron_shells": [2, 8, 18, 32, 29, 8, 2],
    "description": "Einsteinium is a synthetic, highly radioactive element named after Albert Einstein."
  },
  {
    "atomic_number": 100,
    "symbol": "Fm",
    "name": "Fermium",
    "atomic_mass": 257,
    "category": "actinide",
    "electron_configuration": "[Rn] 5f12 7s2",
    "electron_shells": [2, 8, 18, 32, 30, 8, 2],
    "description": "Fermium is a synthetic, radioactive element discovered in the debris of a hydrogen bomb explosion."
  },
  {
    "atomic_number": 101,
    "symbol": "Md",
    "name": "Mendelevium",
    "atomic_mass": 258,
    "category": "actinide",
    "electron_configuration": "[Rn] 5f13 7s2",
    "electron_shells": [2, 8, 18, 32, 31, 8, 2],
    "description": "Mendelevium is a synthetic, radioactive metal named after Dmitri Mendeleev."
  },
  {
    "atomic_number": 102,
    "symbol": "No",
    "name": "Nobelium",
    "atomic_mass": 259,
    "category": "actinide",
    "electron_configuration": "[Rn] 5f14 7s2",
    "electron_shells": [2, 8, 18, 32, 32, 8, 2],
    "description": "Nobelium is a synthetic, radioactive element named in honor of Alfred Nobel."
  },
  {
    "atomic_number": 103,
    "symbol": "Lr",
    "name": "Lawrencium",
    "atomic_mass": 266,
    "category": "actinide",
    "electron_configuration": "[Rn] 5f14 7s2 7p1",
    "electron_shells": [2, 8, 18, 32, 32, 8, 3],
    "description": "Lawrencium is a synthetic, radioactive element named after Ernest O. Lawrence."
  },
  {
    "atomic_number": 104,
    "symbol": "Rf",
    "name": "Rutherfordium",
    "atomic_mass": 267,
    "category": "transition metal",
    "electron_configuration": "[Rn] 5f14 6d2 7s2",
    "electron_shells": [2, 8, 18, 32, 32, 10, 2],
    "description": "Rutherfordium is a synthetic, highly radioactive metal named after Ernest Rutherford."
  },
  {
    "atomic_number": 105,
    "symbol": "Db",
    "name": "Dubnium",
    "atomic_mass": 268,
    "category": "transition metal",
    "electron_configuration": "[Rn] 5f14 6d3 7s2",
    "electron_shells": [2, 8, 18, 32, 32, 11, 2],
    "description": "Dubnium is a synthetic, highly radioactive metal named after Dubna in Russia."
  },
  {
    "atomic_number": 106,
    "symbol": "Sg",
    "name": "Seaborgium",
    "atomic_mass": 269,
    "category": "transition metal",
    "electron_configuration": "[Rn] 5f14 6d4 7s2",
    "electron_shells": [2, 8, 18, 32, 32, 12, 2],
    "description": "Seaborgium is a synthetic, radioactive element named after Glenn T. Seaborg."
  },
  {
    "atomic_number": 107,
    "symbol": "Bh",
    "name": "Bohrium",
    "atomic_mass": 270,
    "category": "transition metal",
    "electron_configuration": "[Rn] 5f14 6d5 7s2",
    "electron_shells": [2, 8, 18, 32, 32, 13, 2],
    "description": "Bohrium is a synthetic, radioactive metal named after physicist Niels Bohr."
  },
  {
    "atomic_number": 108,
    "symbol": "Hs",
    "name": "Hassium",
    "atomic_mass": 269,
    "category": "transition metal",
    "electron_configuration": "[Rn] 5f14 6d6 7s2",
    "electron_shells": [2, 8, 18, 32, 32, 14, 2],
    "description": "Hassium is a synthetic, radioactive element named after the German state of Hesse."
  },
  {
    "atomic_number": 109,
    "symbol": "Mt",
    "name": "Meitnerium",
    "atomic_mass": 278,
    "category": "transition metal",
    "electron_configuration": "[Rn] 5f14 6d7 7s2",
    "electron_shells": [2, 8, 18, 32, 32, 15, 2],
    "description": "Meitnerium is a synthetic, radioactive element named in honor of physicist Lise Meitner."
  },
  {
    "atomic_number": 110,
    "symbol": "Ds",
    "name": "Darmstadtium",
    "atomic_mass": 281,
    "category": "transition metal",
    "electron_configuration": "[Rn] 5f14 6d8 7s2",
    "electron_shells": [2, 8, 18, 32, 32, 16, 2],
    "description": "Darmstadtium is a synthetic, radioactive element named after Darmstadt in Germany."
  },
  {
    "atomic_number": 111,
    "symbol": "Rg",
    "name": "Roentgenium",
    "atomic_mass": 282,
    "category": "transition metal",
    "electron_configuration": "[Rn] 5f14 6d9 7s2",
    "electron_shells": [2, 8, 18, 32, 32, 17, 2],
    "description": "Roentgenium is a synthetic, radioactive element named after Wilhelm Röntgen."
  },
  {
    "atomic_number": 112,
    "symbol": "Cn",
    "name": "Copernicium",
    "atomic_mass": 285,
    "category": "transition metal",
    "electron_configuration": "[Rn] 5f14 6d10 7s2",
    "electron_shells": [2, 8, 18, 32, 32, 18, 2],
    "description": "Copernicium is a synthetic, radioactive metal named after astronomer Nicolaus Copernicus."
  },
  {
    "atomic_number": 113,
    "symbol": "Nh",
    "name": "Nihonium",
    "atomic_mass": 286,
    "category": "post-transition metal",
    "electron_configuration": "[Rn] 5f14 6d10 7s2 7p1",
    "electron_shells": [2, 8, 18, 32, 32, 18, 3],
    "description": "Nihonium is a synthetic, radioactive element named after Japan (Nihon)."
  },
  {
    "atomic_number": 114,
    "symbol": "Fl",
    "name": "Flerovium",
    "atomic_mass": 289,
    "category": "post-transition metal",
    "electron_configuration": "[Rn] 5f14 6d10 7s2 7p2",
    "electron_shells": [2, 8, 18, 32, 32, 18, 4],
    "description": "Flerovium is a synthetic, radioactive element named after the Flerov Laboratory of Nuclear Reactions."
  },
  {
    "atomic_number": 115,
    "symbol": "Mc",
    "name": "Moscovium",
    "atomic_mass": 290,
    "category": "post-transition metal",
    "electron_configuration": "[Rn] 5f14 6d10 7s2 7p3",
    "electron_shells": [2, 8, 18, 32, 32, 18, 5],
    "description": "Moscovium is a synthetic, radioactive element named after Moscow Oblast in Russia."
  },
  {
    "atomic_number": 116,
    "symbol": "Lv",
    "name": "Livermorium",
    "atomic_mass": 293,
    "category": "post-transition metal",
    "electron_configuration": "[Rn] 5f14 6d10 7s2 7p4",
    "electron_shells": [2, 8, 18, 32, 32, 18, 6],
    "description": "Livermorium is a synthetic, radioactive element named after Lawrence Livermore National Laboratory."
  },
  {
    "atomic_number": 117,
    "symbol": "Ts",
    "name": "Tennessine",
    "atomic_mass": 294,
    "category": "halogen",
    "electron_configuration": "[Rn] 5f14 6d10 7s2 7p5",
    "electron_shells": [2, 8, 18, 32, 32, 18, 7],
    "description": "Tennessine is a synthetic, radioactive element named after the state of Tennessee in the United States."
  },
  {
    "atomic_number": 118,
    "symbol": "Og",
    "name": "Oganesson",
    "atomic_mass": 294,
    "category": "noble gas",
    "electron_configuration": "[Rn] 5f14 6d10 7s2 7p6",
    "electron_shells": [2, 8, 18, 32, 32, 18, 8],
    "description": "Oganesson is a synthetic, radioactive element named after Russian physicist Yuri Oganessian."
  }
]


# Dictionary mapping atomic numbers to element data for quick lookup
ELEMENTS_BY_NUMBER = {element["atomic_number"]: element for element in ELEMENTS_DATA}

# Dictionary mapping element symbols to element data for quick lookup
ELEMENTS_BY_SYMBOL = {element["symbol"]: element for element in ELEMENTS_DATA}

# Dictionary mapping element categories to display colors
ELEMENT_CATEGORIES = {
    "nonmetal": "#76FF03",            # Light Green
    "noble gas": "#64FFDA",           # Teal
    "alkali metal": "#FF5252",        # Red
    "alkaline earth metal": "#FF4081",# Pink
    "metalloid": "#FFAB40",           # Orange
    "halogen": "#40C4FF",             # Light Blue
    "post-transition metal": "#BDBDBD", # Gray
    "transition metal": "#FFC107",    # Amber
    "lanthanide": "#CE93D8",          # Light Purple
    "actinide": "#F8BBD0"             # Soft Pink
}


# 2D array representing the layout of the periodic table
# 0 represents an empty cell, numbers represent atomic numbers
PERIODIC_TABLE_LAYOUT = [
    # Period 1 (2 elements, H and He)
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    
    # Period 2 (8 elements, Li through Ne)
    [3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 6, 7, 8, 9, 10],
    
    # Period 3 (8 elements, Na through Ar)
    [11, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 14, 15, 16, 17, 18],
    
    # Period 4 (18 elements, K through Kr)
    [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36],
    
    # Period 5 (18 elements, Rb through Xe)
    [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54],
    
    # Period 6 (18 elements, Cs through Rn)
    # Lanthanum (57) appears here in group 3; the rest of the lanthanides (58–71)
    # are placed in a separate row (see below).
    [55, 56, 57, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86],
    
    # Period 7 (18 elements, Fr through Og)
    # Actinium (89) appears here in group 3; the rest of the actinides (90–103)
    # are placed in a separate row (see below).
    [87, 88, 89, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118],
    
    # Lanthanides (often shown as a “footnote” f-block row for Period 6)
    # These fill the 4f orbitals; La (57) is already placed above.
    [0, 0, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 0, 0],
    
    # Actinides (often shown as a “footnote” f-block row for Period 7)
    # These fill the 5f orbitals; Ac (89) is already placed above.
    [0, 0, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 0, 0]
]
