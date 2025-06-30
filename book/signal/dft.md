(dft)=
# Discrete Fourier Transform

## Discrete time Fourier Transform (DTFT)

We discretize Fourier transform of $x_s(t)$

$$X_s(f)=\int_{-\infty}^{\infty}x_s(t)e^{-j2\pi ft}dt$$

by replacing the integral by summation over time:

$$X_s(f)=\sum_{n=-\infty}^{\infty}\Delta tx_ne^{-j2\pi fn\Delta t}$$

with $x_n=x(n\Delta t)$ and where complex exponential is also evaluated at times $t=n\Delta t$, and $n\in\mathbb{Z}$.

This is still a **continuous function** of frequency $f$ ($f\in\mathbb{R}$), periodic with period $f_s$, exactly as we got with impulse train sampling, and known as Discrete Time Fourier Transform (DTFT).

## Discrete Fourier Transform (DFT)

We want to analyze spectrum $X_s(f)$ of *sampled* signal $x_s(t)$ using a computer, i.e. by Digital Signal Processing (DSP). Two issues remain, however:

$$X_s(f)=\sum_{n=-\infty}^{\infty}\Delta tx_ne^{-j2\pi fn\Delta t}$$

* we cannot measure the signal forever, so we cannot have $n\to\infty$
* once sampled in time domain, still continuous function (of frequency) does not lend itself to DSP - algorithm requires *discrete* data points as input, and delivers *discrete* data points as output

**Action item 1 - we cannot measure signal forever**

Sampled signal $x_s(t)$ is a sequence $x_n$ with $n=\{-\infty,...,\infty\}$, so values $x_n=x(n\Delta t)$ at discrete times $t=n\Delta t$ (with $n\in\mathbb{Z}$).

We consider it only for time duration $T=N\Delta t$, resulting in just N samples; effectively this means applying a window $\Pi\left(\frac{t}{T}\right)$; in practice we set the signal to zero outside window, hence: $x_{sw}(t)=\Pi\left(\frac{t}{T}\right)x_s(t)$

This means $x_n$ with $n=0,...,N-1$ has **finite length**

**Action item 2 - continuous function does not lend itself to DSP**

Sample frequency spectrum: we will evaluate it only at *discrete* frequencies.

As we only use piece of $T=N\Delta t$ of the signal, the *smallest* resulting frequency is known as frequency (or spectral) **resolution** and it is given by

$$f_0=\frac{1}{T}=\frac{1}{N\Delta t}=\frac{f_s}{N}$$

and the *largest* frequency is related to the sampling frequency by $f_s=\frac{1}{\Delta t}$. Hence, the spectrum will be computed at frequencies

$$f=0,\frac{1}{N}f_s,\frac{2}{N}f_s,...,\frac{N-1}{N}f_s$$

This results in the so-called **Discrete Fourier Transform (DFT)**. DFT turns $N$ samples of signal $x(t)$ into $N$ samples of spectrum $X_{sw}(f)$:

$$x(n\Delta t) \leftrightarrow X_{sw}(kf_0)$$

with both $n$ and $k\in\{0,1,...,N-1\}$.

```{admonition} Frequency sampling (background information)
:class: tip

By default, analysis frequencies are $f=0,\frac{1}{N}f_s$,$\frac{2}{N}f_s,...,\frac{N-1}{N}f_s$ or, in terms of the sampling duration, $T$: $f=0,\frac{1}{T},\frac{2}{T},...,\frac{N-1}{T}$

Sampling the spectrum at interval of $\frac{1}{T}$ Hz turns sampled time signal into *periodic* (instead of windowed) signal with period $T$. This choice causes DFT to turn $N$ samples of $x(t)$ into $N$ samples of $X_{sw}(f)$.

Sampling frequency at *higher* rate (smaller interval in frequency) is possible. On the other hand, sampling at *lower* rate is **not allowed**. A longer interval of, e.g. $\frac{2}{T}$ Hz would cause the signal to repeat every $\frac{T}{2}$, thus causing **aliasing** in the time domain
```

Going back to our action items:

**Action item 1**:

Sampled, windowed signal $x_{sw}(t)$ equals sequence $x_n$ with $n=0,1,...,N-1$. Then, $X_{sw}(f)=\int_{-\infty}^{\infty}x_{sw}(t)e^{-j2\pi ft}dt$, which we discretize with step size $\Delta t$ into:

$$X_{sw}(f)=\sum_{n=0}^{N-1}\Delta t\,x_ne^{-j2\pi fn\Delta t}$$

**Action item 2**:

Finally, we sample the frequency spectrum, turning $X_{sw}(f)$ into $X_{sws}(f)$ by considering only $f=k\Delta f$ with $\Delta f=f_0=\frac{1}{T}=\frac{1}{N\Delta t}=\frac{f_s}{n}$ and $k=0,1,...,N-1$:

$$X_{sws}(k\Delta f)=\Delta t\sum_{n=0}^{N-1}x_ne^{-j2\pi k\Delta fn\Delta t}=\Delta t\sum_{n=0}^{N-1}x_ne^{-j\frac{2\pi}{N}kn},\hspace{5px}\text{with }k\in\mathbb{Z}$$

Hence sequence $X_k$ equals $X_{sws}(f)$ at $f=k\Delta f$ for $k=0,1,...,N-1$:

(FFT)=
$$X_k=\Delta t\sum_{n=0}^{N-1}x_ne^{-j\frac{2\pi}{N}kn}$$

This is the discrete Fourier transform (DFT), typically implemented in software packages as `fft` (in Python, we will use `numpy.fft.fft`).

## Inverse Fourier Transform (IDFT)

The Inverse Fourier Transform reads $x(t)=\int_{-\infty}^{\infty}X(f)e^{j2\pi ft}df$. Applying it to the sequence $X_k$ and discretizing the integral yields:

$$x_{sws}(t)=\sum_{k=0}^{N-1}\Delta fX_ke^{j2\pi k\Delta ft}$$

Considering sampling in the time domain as $t=n\Delta t$:

$$x_n=\sum_{k=0}^{N-1}\Delta fX_ke^{j2\pi k\Delta fn\Delta t}=\Delta f\sum_{k=0}^{N-1}X_ke^{j\frac{2\pi}{N}kn}=\frac{1}{N\Delta t}\sum_{k=0}^{N-1}X_ke^{j\frac{2\pi}{N}kn}$$

## Summary

$$\begin{gather*}X_k=\Delta t\sum_{n=0}^{N-1}x_ne^{-j\frac{2\pi}{N}kn}\\ x_n=\frac{1}{N\Delta t}\sum_{k=0}^{N-1}X_ke^{j\frac{2\pi}{N}kn}\end{gather*}$$

with both $k$ and $n\in\{0,1,...,N-1\}$

With $X_k$, we consider function $X(k\Delta f)$ by restoring *frequency dimension*, frequency resolution, $\Delta f=f_0=\frac{1}{T}=\frac{1}{N\Delta t}=\frac{f_s}{N}$

With $x_n$, we consider function $x(n\Delta t)$ by restoring time dimension, with time resolution $\Delta t=\frac{1}{f_s}$

In many textbooks we also find DFT as:

$$\begin{gather*}X_k=\sum_{n=0}^{N-1}x_ne^{-j\frac{2\pi}{N}kn}\\ x_n=\frac{1}{N}\sum_{k=0}^{N-1}X_ke^{j\frac{2\pi}{N}kn}\end{gather*}$$

with both $k$ and $n\in\{0,1,...,N-1\}$

Hence, *without* factors $\Delta t$ and $\frac{1}{\Delta t}$. This is also how DFT is implemented in programming languages like Matlab and Python; the user has to restore time and frequency dimension!

