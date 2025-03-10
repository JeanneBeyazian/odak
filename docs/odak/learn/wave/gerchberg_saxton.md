# odak.learn.wave.gerchberg_saxton

::: odak.learn.wave.gerchberg_saxton
    selection:
        docstring_style: numpy

## Notes

To optimize a phase-only hologram using Gerchberg-Saxton algorithm, please follow and observe the below example:

```
import torch
from odak.learn.wave import gerchberg_saxton
from odak import np
wavelength              = 0.000000532
dx                      = 0.0000064
distance                = 0.2
target_field            = torch.zeros((500,500),dtype=torch.complex64)
target_field[0::50,:]  += 1
iteration_number        = 3
hologram,reconstructed  = gerchberg_saxton(
                                           target_field,
                                           iteration_number,
                                           distance,
                                           dx,
                                           wavelength,
                                           np.pi*2,
                                           'TR Fresnel'
                                          )
```



## See also

* [`Computer Generated-Holography`](../../../cgh.md)
* [`odak.learn.wave.stochastic_gradient_descent`](stochastic_gradient_descent.md)
* [`odak.learn.wave.point_wise`](point_wise.md)
