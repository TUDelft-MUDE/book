# Sampling

## Discrete and Quantized signals

**Discrete signals**

A **discrete** signal has a value only at discrete values of the running variable (usually time). Formally the signal is then to be referred to as *discrete-time* signal. The interval between these discrete values of running variable is often uniform, e.g. $\Delta t$. In between these values, the signal may be zero, undefined, or of no interest!

```{note}

**Continuous-time** signal is written as $x(t)$. A **discrete-time** signal is usually written as $x[n]$, or $x_n$ (sequence $x_0$, $x_1$, $x_2$...)

```

![discrete](https://files.mude.citg.tudelft.nl/discrete.png "discrete")

**Continuous signals**

A **quantized** signal may assume only countable number of values. Yet, changes from value to value may occur at any time. Think of describing an analog signal with 2 bits! The description of that signal can only have 4 possible values: ```00```, ```01```, ```10``` and ```11```, which represent the values 0, 1, 2 and 3 in the figure below.

![quantized](https://files.mude.citg.tudelft.nl/quantized.png "quantized")

When we have more bits available, like 8, the signal description may have $2^8=256$ possible values. Clearly, the number of available bits defines the **resolution** of the quantization.

## Singularity function

### Unit impulse

A very important function for sampling is the **unit-impulse** or **Dirac-delta** function:

$$
\delta(t)=0,
\hspace{10px} t\neq 0
\hspace{10px} \textrm{and} \hspace{10px} 
\int_{-\infty}^{\infty}\delta(t)dt=1
$$

and its graph looks like:

![dirac](https://files.mude.citg.tudelft.nl/dirac.png "dirac")

The **area** of the function equals 1, and this area is obtained in **infinitesimal** interval of time. We use this function to represent phenomena that occur in **very short time intervals** compared to resolution capability of measuring device, but which produce almost instantaneous change in measured quantity.

However, no conventional function exists with properties of the Dirac delta pulse. Let us define:

$$\delta_{\epsilon}=\frac{1}{2\epsilon}\Pi\left(\frac{t}{2\epsilon}\right)=\begin{cases}\frac{1}{2\epsilon}:|t|\leq\epsilon\\0:|t|>\epsilon\end{cases}$$

![real_delta](https://files.mude.citg.tudelft.nl/real_delta.png "real_delta")

where $\epsilon\to 0$ yields a **unit impulse** function.

### Sifting property

A very useful property of the Dirac delta function is the **sifting property**:

$$\int_{-\infty}^{\infty}x(t)\delta(t-t_0)dt=x(t_0)$$

![sifting](https://files.mude.citg.tudelft.nl/sifting.png "sifting")

The conclusion is that this blue area equals $x(t_0)$ (in the above diagram $\epsilon=1$ was taken).

## Analog-to-digital conversion

Sampling can be modelled by multiplication of continuous-time signal $x(t)$ with sampling function $p(t)$.

![atod](https://files.mude.citg.tudelft.nl/atod.png "atod")

The sampled signal then becomes $x_p(t)=x(t)p(t)$.

The sampling function, $p(t)$, is assumed to be periodic pulse train with **sampling period** $\Delta t$ (note that earlier, $T$ or $T_0$ denoted the period of a periodic signal).

In practice, time during which $p(t)$ is non-zero (pulse width) is very small relative to period $\Delta t$.

In fact, in digital systems, where sample is the number corresponding to the value of the signal $x(t)$ at the sampling instant, $t$, the **pulse width** of the sampling function is **infinitelly small**. Hence, we can model the sampling funtion as an **impulse train**

![impulse_train](https://files.mude.citg.tudelft.nl/impulse_train.png "impulse_train")

## Fourier transform of sampled signal

The impulse train $p(t)=\sum_{n=-\infty}^{\infty}\delta(t-n\Delta t)$ is periodic ($n\in\mathbb{Z}$), with fundamental period $\Delta t$, and can be written as Fourier series:

$$p(t)=\sum_{k=-\infty}^{\infty}P_ke^{j2\pi kf_0t},\hspace{5px}\text{with }k\in\mathbb{Z}$$

With fundamental frequency $f_0=\frac{1}{\Delta t}=f_s$ (the sampling frequency), and Fourier coefficients $P_k$ as:

$$P_k=\frac{1}{\Delta t}\int_{-\frac{\Delta t}{2}}^{\frac{\Delta t}{2}}p(t)e^{-j2\pi kf_0t}dt=\frac{1}{\Delta t}\int_{-\frac{\Delta t}{2}}^{\frac{\Delta t}{2}}\delta(t)e^{-j2\pi kf_0t}dt=\frac{1}{\Delta t}=f_s$$

using the sifting property, and considering only one impulse occuring in the integration interval (at $t=0$). The Fourier series of $p(t)$ then becomes:

$$p(t)=f_s\sum_{k=-\infty}^{\infty}e^{j2\pi kf_st}$$

In the time domain, sampling is modelled as:

$$x_s(t)=\Delta tx(t)p(t)$$

multiplied with $\Delta t=\frac{1}{f_s}$ as a *correction factor* (to restore correct dimension; $p(t)$ has dimension [1/s] and we want signal $x_s(t)$ to have the same dimension as $x(t)$ itself).

Now, what happens to the spectrum $X(f)$ of signal $x(t)$ when it gets impulse train-sampled? What is $X_s(f)$ of $x_s(t)$?

:::{card} Derivation

```{admonition} MUDE Exam Information
:class: tip, dropdown
This derivation is provided for additional insight and will not be part of the exam.
```

The Fourier transform of $x_s(t)$ is:

$$X_s(f)=\int_{-\infty}^{\infty}\Delta tx(t)p(t)e^{-j2\pi ft}dt$$

Using the Fourier series of $p(t)$:

$$X_s(f)=\Delta t\int_{-\infty}^{\infty}\left(f_s\sum_{k=-\infty}^{\infty}e^{j2\pi kf_st}\right)x(t)e^{-j2\pi ft}dt$$

Interchanging integration and summation:

$$\begin{align}X_s(f)&=\underbrace{\Delta tf_s}_{1}\sum_{k=-\infty}^{\infty}\int_{-\infty}^{\infty}x(t)e^{j2\pi kf_st}e^{-j2\pi ft}dt=\\&=\sum_{k=-\infty}^{\infty}\underbrace{\int_{-\infty}^{\infty}x(t)e^{-j2\pi(f-kf_s)t}dt}_{X(f-kf_s)}\end{align}$$

:::

Finally, the Fourier transform of the *sampled* signal becomes:

$$X_s(f)=\sum_{k=-\infty}^{\infty}X(f-kf_s), \hspace{10px}\textrm{with }\,k\in\mathbb{Z}$$

so, the spectrum of the sampled signal is the spectrum of the original signal, but repeated with "period" $f_s$ (in the frequency domain); copies of spectrum are called _aliases._

| ![sampled](https://files.mude.citg.tudelft.nl/sampled.png "sampled") |
| :--: |
| *Spectrum of an assumed original signal $x(t)$ (left) and that of its sampled equivalent (right)* |

## Sampling Theory

In practice, we should choose a _sample rate_ that is capable of representing the frequency components of a continuous signal as a discrete sequence. The term _rate_ is quantified in units of samples per second, whereas a _frequency_ component of the signal is described using cycles per second; both are represented by units of frequency, Hertz (Hz).

Consider a **band-limited** signal, $x(t)$, which has no frequency components above $f_h$ Hz. Such a signal can be *completely specified* by samples taken at a *uniform* sample rate greater than $2f_h$ Hz.

```{admonition} Definition: Nyquist *rate* and Nyquist *frequency.*

If $f_h$ is the maximum frequency of a band-limited signal, the quantity $2f_h$ is called the **Nyquist rate.**

If the same signal is sampled at rate $f_s$, the quantity $f_s/2$ is called the **Nyquist frequency.**

Note that the Nyquist _rate_ is related to the _frequency_ of a signal, and the Nyquist _frequency_ is related to the sampling. In other words, the Nyquist rate is characteristic of the signal, whereas the Nyquist frequency is characteristic of the sampling system!

In practice we consider only the domain $-\frac{f_s}{2}<f<\frac{f_s}{2}$ of the spectrum obtained from the sampled signal.

```

Although many signals in practice are not band-limited, by considering the maximum frequency of interest for a particular application, the Nyquist rate can be applied to determine a suitable sampling strategy; specifically, to avoid aliasing.

## Aliasing

Note that in order to reconstruct original continuous-time signal from samples, it is crucial to **sample the signal at a rate larger than Nyquist rate**. When sampling is below this rate, the adjacent spectra (aliases) will overlap, and it will be impossible to reconstruct the signal from its samples. This phenomenon is called **aliasing**, and is illustrated in the following two examples.

```{admonition} Theoretical Example

As an example, we will study the effect of sampling a sinusoidal signal with frequency $f_c=5$ Hz we have $x(t)=6\cos(10\pi t)$

![first](https://files.mude.citg.tudelft.nl/first.png "first")

First, we look at the *correctly* sampled signal, with $f_s=14$ Hz ($f_s>2f_c$). The spectrum (which is real, because $x(t)$ is even) of original continuous-time signal will have two Dirac-functions with weight 3, at $f=5$ Hz and $f=-5$ Hz, i.e.

$$X(f)=\frac{6}{2}(\delta(f-5)+\delta(f+5))$$

Sampled at 14 Hz, we find:

![sampled2](https://files.mude.citg.tudelft.nl/sampled2.png "sampled2")

**Spectrum**

With $x(t)=6\cos(10\pi t)$ and $f_s=14$ Hz:

$$X_s(f)=3\sum_{k=-\infty}^{\infty}(\delta(f+5-kf_s)+\delta(f-5-kf_s)), \hspace{5px}\text{with }k\in\mathbb{Z}$$

![sampling3](https://files.mude.citg.tudelft.nl/sampling3.png "sampling3")

The dashed lines indicate integer multiples of the sampling frequency. As we are only considering the domain $-\frac{f_s}{2}<f\leq\frac{f_s}{2}$:

![sampled4](https://files.mude.citg.tudelft.nl/sampled4.png "sampled4")

And we see that with this sampling we get a **correct result** (just the two original Dirac delta pulses in blue)!

![sampling5](https://files.mude.citg.tudelft.nl/sampling5.png "sampling5")

*But what if we try to sample our signal using a sampling frequency of 7 Hz?*

Well, with this we violate the sampling theorem, as $f_s=7$ Hz and, therefore, $f_s\ngeq 2f_c$. We find:

![sampling6](https://files.mude.citg.tudelft.nl/sampling6.png "sampling6")

With this, we find the following spectrum:

![sampling7](https://files.mude.citg.tudelft.nl/sampling7.png "sampling7")

Once again, considering only the domain $-\frac{f_s}{2}<f\leq\frac{f_s}{2}$ represented in grey, we find:

![sampling8](https://files.mude.citg.tudelft.nl/sampling8.png "sampling8")

And we see we find an **incorrect result**, as the sampled and reconstructed signal (in dashed green) presents a lower frequency than the original signal (in blue) we encounter Dirac delta pulses in green and red at 2 Hz and -2 Hz:

![sampling9](https://files.mude.citg.tudelft.nl/sampling9.png "sampling9")

```

````{admonition} Example in Practice

The phenomenon illustrated in this video is known as the "wagon wheel effect," and, more generally as the _stroboscopic effect_ (and you can find loads of videos on it in addition to the one her). This phenomenon is a result of aliasing.

```{eval-rst}
.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/TkPT9ataS-Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

Suppose you have a wheel with, hypothetically, only one spoke connecting the rim to the axle. By watching the spoke we can tell whether, and how, the wheel is turning. If this wheel would be turning at a frequency of $f_c$ = 1 cycle per second (Hz), and we would capture frames with a video camera at exactly $f_s$ = 1 Hz (one frame per second), then we would see the spoke in exactly the same position in all frames recorded by the camera; hence, it looks like the wheel is standing still in our video! Of course in reality the wheel is turning. In this case the video, a series of images taken at discrete time instants, gives us a false impression about reality.

Connecting this to Nyquist sampling: the wheel rotation frequency is $f_c$ = 1 Hz, and hence the Nyquist rate is 2 Hz, and our sampling frequency $f_s$ = 1 Hz is clearly below it (we're sampling too slowly). The spectrum (with frequencies $f_c$ = -1 and +1 Hz) gets copied to integer multiples of the sampling frequency $f_s$ (e.g. at 1 Hz), hence a copy of $f_c$ = -1 Hz, shows up as an alias at $f$ = 0 Hz.

The example in the video is slightly more involved as the wheel has 7 identical spokes, causing the frequency of interest ($f_c$) to be actually 7 times as large. We achieve an identically looking image already after 1/7th turn of the wheel.

In the video, at some point, the wheel is turning backward: not in reality, but in our observations based on the sampled signal. At this point we were driving slightly over 30 km/h, which is 8.9 m/s. With a wheel circumference of 1.92 m, the turning frequency is 4.6 Hz. With 7 identical spokes, the periodic signal has a frequency of 7 times 4.6 Hz, which yields $f_c$ = 32.4 Hz. The camera on the smartphone captures the video at 30 frames per second (fps), hence $f_s$ = 30 Hz. So, we can expect an alias of $f_c$ at a frequency of -2.4 Hz (a negative frequency, materialized by the apparently a backward turning wheel).

````

## Summary

The Fourier transform of a **sampled signal**, $x_s(t)$, is given as:

$$X_s(f)=\sum_{k=\infty}^{\infty}X(f-kf_s)$$

where $f_s$ is the sampling frequency.

To prevent aliases, this frequency $f_s$ should be larger than $2f_h$, where $f_h$ is the highest frequency occurring in the signal!

## Exercises

Given a signal $x(t)$ that is sampled at frequency $f_s$, what does $X_s(f)$ look like? The following quiz questions will test your knowledge.

<iframe src="https://tudelft.h5p.com/content/1292121772554459737/embed" aria-label="Sampling Quiz" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe><script src="https://tudelft.h5p.com/js/h5p-resizer.js" charset="UTF-8"></script>
