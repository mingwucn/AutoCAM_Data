# Synthetic spherical turning band regression fixtures

These four generated STEP cases bind the original and translated complete
spheres, each with zero or 0.5 mm finishing allowance, to exact native preparation
and recording outputs. The accompanying UI browser test runs the actual CAD and
Python workers and compares 27 ordered action states plus saved/restored decisions.

`release.json` pins the 27 test input files. `inputs.json` records their source
stage identity and expected shared Python archive. Fixture expectations are not
substituted for simulation responses. The origin allowance case remains incomplete;
the other three meet their declared roughing objective, not finishing qualification.

Runtime assets are separately indexed in `releases/adaptive-spherical-bands-v1`.
Previous releases remain unchanged. These are synthetic development cases, not
industrial manufacturing qualification or trained-policy quality evidence.
