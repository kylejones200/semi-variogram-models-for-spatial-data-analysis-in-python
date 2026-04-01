# Semi-Variogram Models for Spatial Data Analysis in Python

Semi-variograms help us analyze how similar observations are based on
how close the observations are to each other. This is a foundational...

### Semi-Variogram Models for Spatial Data Analysis in Python
Semi-variograms help us analyze how similar observations are based on
how close the observations are to each other. This is a foundational
concept for geostatistics. A semi-variogram quantifies how the
similarity between observations changes with distance. On its vertical
axis, it shows the semi-variance γ(h), a measure of dissimilarity, while
the horizontal axis represents distance (lag) h. The shape of the curve
tells us how spatial correlation behaves in the dataset.

Choosing the right semi-variogram model matters because it influences
interpolation methods such as kriging, determines how far spatial
influence extends, and shapes the uncertainty estimates.

### De Wijsian Model
**Equation:** γ(h) = A ln(h) + B

**Behavior:** This model is *mildly non-stationary*. The semi-variance
increases without bound as distance grows, but the growth slows
logarithmically. This can fit processes where spatial dependence
persists over long ranges but weakens slowly --- such as pollution
levels downwind of an industrial site or the spread of cultural
influence over a large region.

A nonzero B indicates a nugget effect, representing measurement error or
micro-scale variation that occurs even between points very close
together.

This is useful when there is long-range dependence without a clear upper
bound or when variability accumulates slowly over distance.


**De Wijsian Model in Mineral Exploration**

Phenomenon: Trace mineral concentration in a river basin downstream of a
mine.

Why this model: Contaminant transport in rivers often has *long-range
dependence*. Even far from the source, concentrations remain correlated
due to persistent sediment-bound particles. The De Wijsian model, which
grows logarithmically without an upper bound, fits this slow, steady
decay of similarity.

Implication: Using a bounded model here would underestimate downstream
contamination risk.

### Linear Model
**Equation:** γ(h) = A h + B

**Behavior:** A *strongly non-stationary* model. The semi-variance
increases linearly with distance, with no plateau. It is simple and can
describe trends where dissimilarity grows steadily across space --- like
soil property changes across a large climatic gradient.

A nonzero B again signals a nugget effect.

This is useful when there is strong spatial drift or gradient or when
you cannot assume a maximum range of spatial influence.


**Linear Model in Urban Housing Prices**

Phenomenon: Housing prices across a metropolitan area with a steady
distance-from-center gradient.

Why this model: When there's a consistent trend --- like prices falling
by a fixed amount per kilometer from the city center --- the linear
semi-variogram reflects the unbounded increase in dissimilarity with
distance.

Implication: A stationary model would smooth away the gradient,
overestimating prices on the outskirts and underestimating them
downtown.

### Log--Log Model
**Equation:** γ(h) = B + h\^A

**Behavior:** Also *strongly non-stationary*. The growth rate of γ(h)
depends on the exponent A. If A \< 1, the curve rises quickly at first
and then slows; if A \> 1, the increase accelerates. Useful for
processes with power-law scaling, such as settlement sizes or vegetation
patchiness in semi-arid landscapes.

This is useful when there is power-law behavior in spatial variance or
when the systems show clustering at multiple scales.


**Log--Log Model in Vegetation Patchiness**

Phenomenon: Vegetation cover in semi-arid rangelands.

Why this model: Patch sizes follow a power-law distribution, with small
clusters common and large clusters rare but influential. The log--log
model captures this scaling, especially when the exponent A is less than
1.

Implication: Correctly modeling the scaling improves predictions for
areas with sparse field measurements, guiding sustainable grazing plans.

### Exponential Model
**Equation:** γ(h) = C₀ + C \[1 --- exp(--\|h\| / a)\]

**Behavior:** A *stationary* model with an asymptotic approach to a sill
(C₀ + C). The parameter a controls how quickly the curve reaches the
sill, which represents the point beyond which additional distance adds
little to dissimilarity.

This model is common in environmental sciences, describing processes
such as temperature variation, rainfall patterns, or soil nutrient
levels where correlation declines exponentially with distance.

This is useful when the spatial influence decays quickly but not
instantly or when the data suggests a well-defined maximum variance at a
finite distance.


**Exponential Model in Air Pollution Monitoring**

Phenomenon: Nitrogen dioxide (NO₂) concentrations in a city.

Why this model: Pollution from traffic sources tends to decay
exponentially with distance. The exponential model reaches its sill
relatively quickly, matching the fact that NO₂ levels at two points a
few kilometers apart are nearly uncorrelated.

Implication: Accurately identifying the short range of correlation
avoids oversampling in low-value areas and directs resources to denser
monitoring near pollution sources.

### Hole Effect Model
**Equation:** γ(h) = C \[1 --- sin(ah) / (ah)\]

**Behavior:** This model produces oscillations as h increases,
suggesting spatial periodicity --- dissimilarity rises, then falls, then
rises again. It can represent patterns like dune spacing, wave-driven
sediment deposits, or periodic urban layouts.

This is useful when there are detectable spatial cycles or repeating
patterns or when there is an oscillating correlation structure.


**Hole Effect Model in Agricultural Field Patterns**

Phenomenon: Soil moisture across an irrigated farm with alternating wet
and dry rows.

Why this model: The hole effect's oscillations fit periodic
variation --- peaks and troughs in the variogram mirror the wet-dry
pattern at regular intervals.

Implication: Recognizing the periodicity prevents kriging from smoothing
away the irrigation structure, allowing better alignment of planting
schedules with moisture availability.

### Spherical Model
**Equation:**

γ(h) = 0 h = 0\
γ(h) = C \[3h / (2a) --- (h³ / (2a³))\] + C₀ h ≤ a\
γ(h) = C + C₀ h \> a

**Behavior:** Another *stationary* model, very popular in practice. It
rises smoothly and reaches the sill exactly at range a. Beyond a,
dissimilarity stops increasing --- points are uncorrelated.

This is the workhorse model for kriging in many environmental and social
science applications. It handles phenomena like heavy metal
concentration in soils, school test score patterns in metropolitan
areas, or vegetation cover in agricultural landscapes.

This is useful when there is smooth correlation decay up to a
well-defined range or when there is no strong reason to choose another
model.


**Spherical Model in Soil Nutrient Mapping**

Phenomenon: Phosphorus concentration in cropland soils.

Why this model: Soil nutrients often show a well-defined correlation
range --- beyond a certain distance, samples are independent. The
spherical model fits this pattern, rising smoothly to the sill at a
finite range.

Implication: Sampling strategies can be optimized so that no two samples
within the range are redundant, saving time and cost.

### Gaussian Model
**Equation:** γ(h) = C₀ + C \[1 --- exp(--3h² / a²)\]

**Behavior:** Stationary, with a very smooth rise from the origin. The
Gaussian model implies high continuity at short distances --- ideal for
processes with gentle spatial variation such as groundwater levels or
temperature in homogeneous terrain.

This is useful when you have highly continuous spatial fields or the
short-distance correlation is especially strong.


**Gaussian Model in Groundwater Level Monitoring**

Phenomenon: Groundwater depth in a homogeneous aquifer.

Why this model: The Gaussian model rises very smoothly from the origin,
reflecting the high continuity of groundwater levels over short
distances.

Implication: Using a model with a sharper rise would overstate
short-range variability, producing unrealistic small-scale fluctuations
in the interpolated surface.

### Choosing the Right Model
Model choice depends on both the empirical semi-variogram and domain
knowledge. The curve's initial slope, whether it levels off, and whether
it oscillates all matter. In environmental monitoring, exponential and
spherical models dominate, but in social sciences, non-stationary models
may be more appropriate for phenomena with large-scale gradients.


<figcaption>This figure illustrates why the choice matters. The
exponential model levels off quickly, the Gaussian rises slowly, and the
De Wijsian never plateaus. Those differences directly influence your
maps and predictions.</figcaption>


### Fitting and Validation
Fitting involves estimating model parameters (nugget, sill, range, and
any exponents) to match the empirical semi-variogram from your data.
Cross-validation --- removing some data points, predicting them with the
model, and checking errors --- is essential to ensure the chosen model
supports reliable spatial predictions.

When fitting a semi-variogram to your data:

1\. Start with the empirical semi-variogram. Plot γ(h) against h from
your data to see if it appears to level off, oscillate, or grow without
bound.

2\. Match model behavior to your understanding of the process.
Environmental transport models, economic gradients, and social network
spillovers all leave distinct signatures.

3\. Validate with cross-validation. Remove some data, predict them with
kriging using your fitted model, and check prediction errors.

### Why It Matters
A semi-variogram model is more than a mathematical curve --- it encodes
assumptions about how your world works. In kriging, it directly shapes
your interpolated surface and uncertainty estimates. In simulation, it
controls the patterns of synthetic spatial fields. For social
scientists, it can uncover the spatial reach of neighborhood effects;
for environmental scientists, it can define how far a pollutant plume
extends.

Choosing well means your spatial analysis rests on a realistic picture
of spatial dependence.

Semi-variograms bridge statistical modeling and real-world process
understanding. They are not arbitrary curve fits --- they are statements
about how far influence reaches, how quickly it fades, and whether it
repeats in space.

```python
import numpy as np
import matplotlib.pyplot as plt

# ---------- Minimalist style ----------
plt.rcParams.update({
    "font.family": "serif",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": False,
})

def style_ax(ax, xlabel="h", ylabel="γ(h)"):
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    # Bracket-like look
    ax.spines["left"].set_position(("outward", 6))
    ax.spines["bottom"].set_position(("outward", 6))
    ax.tick_params(axis="both", which="both", direction="out")
    return ax

# ---------- Semi-variogram models ----------
def de_wijsian(h, A=0.6, B=0.0):
    h_safe = np.where(h == 0, 1e-9, h)
    return A * np.log(h_safe) + B

def linear(h, A=0.4, B=0.0):
    return A * h + B

def log_log(h, A=0.7, B=0.0):
    return B + np.power(h, A)

def exponential(h, C0=0.1, C=1.0, a=10.0):
    return C0 + C * (1.0 - np.exp(-np.abs(h) / a))

def hole_effect(h, C=1.0, a=0.7):
    x = a * h
    # γ(h) = C[1 - sin(ah)/(ah)], with limit 0 at h=0
    sinc = np.where(x == 0, 1.0, np.sin(x) / x)
    return C * (1.0 - sinc)

def spherical(h, C0=0.0, C=1.0, a=10.0):
    h = np.asarray(h)
    y = np.empty_like(h, dtype=float)
    inside = h <= a
    x = h[inside] / a
    y[inside] = C0 + C * (1.5 * x - 0.5 * x**3)
    y[~inside] = C0 + C
    return y

def gaussian(h, C0=0.1, C=1.0, a=10.0):
    return C0 + C * (1.0 - np.exp(-3.0 * (h**2) / (a**2)))

# ---------- Plot helpers ----------
def plot_model(h, gamma, name, fname, ylim=None):
    fig, ax = plt.subplots(figsize=(6, 3.2))
    ax.plot(h, gamma, linewidth=2)
    style_ax(ax)
    ax.set_title(name)
    if ylim is not None:
        ax.set_ylim(*ylim)
    ax.margins(x=0)
    fig.tight_layout()
    plt.savefig(fname, dpi=200, bbox_inches="tight")
    plt.show()

# ---------- Build curves ----------
if __name__ == "__main__":
    # Non-stationary: use a compact domain that shows growth
    h_ns = np.linspace(1e-3, 30, 600)

    plot_model(h_ns, de_wijsian(h_ns, A=0.8, B=0.2), "De Wijsian", "semivariogram_de_wijsian.png")
    plot_model(h_ns, linear(h_ns, A=0.06, B=0.0), "Linear", "semivariogram_linear.png")
    plot_model(h_ns, log_log(h_ns, A=0.6, B=0.1), "Log–Log", "semivariogram_loglog.png")

    # Stationary: show approach to sill over ~3 ranges
    a = 10.0
    h_s = np.linspace(0, 3 * a, 600)

    plot_model(h_s, exponential(h_s, C0=0.05, C=1.0, a=a), "Exponential", "semivariogram_exponential.png", ylim=(0, 1.2))
    plot_model(h_s, hole_effect(h_s, C=1.0, a=0.7), "Hole Effect", "semivariogram_hole_effect.png")
    plot_model(h_s, spherical(h_s, C0=0.05, C=1.0, a=a), "Spherical", "semivariogram_spherical.png", ylim=(0, 1.2))
    plot_model(h_s, gaussian(h_s, C0=0.05, C=1.0, a=a), "Gaussian", "semivariogram_gaussian.png", ylim=(0, 1.2))
```
::::::::By [Kyle Jones](https://medium.com/@kyle-t-jones) on
[August 10, 2025](https://medium.com/p/a44b3eb6e092).

[Canonical
link](https://medium.com/@kyle-t-jones/semi-variogram-models-for-spatial-data-analysis-in-python-a44b3eb6e092)

Exported from [Medium](https://medium.com) on November 10, 2025.
