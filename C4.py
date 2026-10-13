# Calculates unloaded and loaded output voltage of a voltage divider when a load resistor rl is connected in parallel with r2.
def loaded_divider(vs,r1,r2,rl):
    unloaded=vs * r2 / (r1 + r2)
    r2_parallel=(r2 * rl) / (r2 + rl)   
    loaded=vs * r2_parallel / (r1 + r2_parallel)
    return round(unloaded,2), round(loaded,2)
print("loaded_divider(12, 1000, 1000, 500) ->", loaded_divider(12,1000,1000,500))
