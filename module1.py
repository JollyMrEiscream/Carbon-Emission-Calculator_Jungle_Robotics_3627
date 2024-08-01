elec_factor = {'coal':935, 'natural gas':500, 'oil':800, 'biomass':60, 'wind':11, 'solar power':45, 'hydropower':15, 'nuclear':15}
materials_factor = {'plastic':2.7, 'rubber':3.5, 'aluminum':12, 'steel':2.15, 'polycarbonate':7.35,'copper wires':4.25}
transportation_factor = {'gasoline cars':185, 'diesel cars':150, 'hybrid cars':85, 'ev':0, 'diesel bus': 1000, 'natural gas buses':850, 'electrical bus':0}
waste_factor = 700

print("This is a wonderful carbon emissions calculator.")
elec_kind = input("What kind of energy did we use? Coal, Natural Gas, Oil, Biomass, Wind, Solar power, Hydropower, Nuclear: ").strip().lower()
electricity_consumption = input("How many kWh of electricity did we use?: ").strip()
elec_emi = elec_factor[elec_kind] * int(electricity_consumption)
print("The total emission for electricity is " + str(elec_emi))

material_kind = input("What materials did we use this year? Please do not use any spaces, but use commas to separate each material. Plastic, Rubber, Aluminum, Steel, Polycarbonate, Copper Wires:  ").lower()
material_kind = [x.strip() for x in material_kind.split(',')]
material_em_list = []

for material in material_kind:
    if material in materials_factor:
        quantity = input(f"How much of {material} did you use (in kilograms)?: ").strip()
        material_emission = materials_factor[material] * float(quantity)
        material_em_list.append(material_emission)
    else:
        print(f"Material '{material}' not found in materials_factor dictionary.")

print(material_em_list)

material_em = sum(material_em_list)
