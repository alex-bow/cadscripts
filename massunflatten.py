# USAGE: Make subdirs dxfs/ stls/ and svgs/
# Place all dxf files to unflatten in dxfs/

from pathlib import Path
import sys
import cadquery as cq


dxfs = Path('./dxfs')
for d in dxfs.iterdir():
    try:
        print("Unflattening " + d.name + "...")
        base = cq.importers.importDXF(d).wires().toPending().extrude(0.4)
        f = d.name.split(".")[0] + ".stl"
        cq.exporters.export(base, "stls/" + d.name.split(".")[0] + ".stl")
    except Exception as e:
        print("Could not automatically unflatten " + d.name + ":")
        print(e)