# ECE 466: Digital Signal Processing, Spring 2022
*Course Website: [d2l.msu.edu/d2l/home/1382712](https://d2l.msu.edu/d2l/home/1382712)*
- [ECE 466: Digital Signal Processing, Spring 2022](#ece-466-digital-signal-processing-spring-2022)
- [Course Description and Policies](#course-description-and-policies)
  - [What You Will Learn:](#what-you-will-learn)
- [Requirements:](#requirements)
- [Schedule](#schedule)

---
__Instructor:__ Seyyid Emre Sofuoglu, sofuoglu@msu.edu. You can reach me from D2L e-mail.

__Lecture Hours:__ TTh 10:20-11:40 am, Wilson Hall C1

__Office Hours:__ TTh 4-5 pm, online. See D2L calendar or announcements for Zoom link.

__Textbook:__ J.R. Deller, Jr., Discrete-Time Signal Processing with Speech Processing Motivations, Vol. 1: Deterministic Signals, &copy; Author, 2016. Posted on class web site

__Reference Books:__ No need to buy them, still they're great for reference and independent study. You can find these in the library.
1. Digital  Signal  Processing,  J.  G.  Proakis  and  D.  G.  Manolakis,  Prentice  Hall, 3rd Edition. Secondary book. (P&M)
2. Discrete-Time Signal Processing, A. V. Oppenheim and R. W. Schafer, Prentice 
Hall.
3. [PySDR: A Guide to SDR and DSP using Python](https://pysdr.org/index.html), Mark Lichtman. This one is great, hosted on web and has lots of tools for DSP on Python. Only Chapter 2 is relevant.

__Prerequisites:__ ECE 366, Introduction to Signal Processing or equivalent.

---
Course Description and Policies 
=

This course introduces fundamental tools for extracting information 
embedded in digital signals. Digital signal processing is performed (after analog-to-digital conversion) due to the cost effectiveness, reliability, and re-configurability of digital hardware and software. Digital Signal Processing (DSP) techniques will specifically be presented in both the time-domain and frequency-domain to analyze signals and systems. To supplement this theory, practical experience in analyzing and processing digital signals will be provided through a computer project based on Python. Digital signal processing is heavily utilized in virtually all aspects of science and engineering. Applications of digital signal processing include machine learning, the study of biological, chemical, social (__Pandemic tracking and prediction__), and physical systems (_even a building is a system_), financial markets, the design of control and communication systems, ...

## What You Will Learn:
1. Relationships between Digital and Analog Systems. Why use digital?
2. Time domain and frequency domain analysis of digital systems. How to better understand, analyze and model digital systems?
3. Tools and skillset for digital signal processing. Operators that correspond to their counterparts of analog signal processing, such as Fourier transform, convolution, ...
4. Theoretical analysis of these tools using $z$-transfom. How does all these work in math?
5. Machine Learning for SP. 

Requirements: 
==
There will be two midterms (50%), homeworks (15%), quizzes (10%), and a final project (25%).
1. __Midterm 1:__ February 17th, Thursday, Class time.
2. __Midterm 2:__ April 5th, Tuesday, Class time.
3. __Final Project:__ (TBD)

---
Schedule
=

| Week | Subjects | Textbook Reference | Notes|
|-|-|-|-|
| 1.10 |  Introduction, Basic Signals & Systems Concepts: Analog vs Digital Signals | Deller, Chapters 0:1, 1:1; P&M, Chapter 1.1, 1.2 |
| 1.17 |  Discrete Time Signal & Systems Concepts: Power, Energy, Classification of Systems.  |  Deller, Chapters 1:1, 5:1-2; P&M, Chapter 1.3-4, 2.1-2 | Hw 1 |
| 1.24 |  Time-domain Analysis: Convolution Sum, Difference Equations |  Deller, 5:3; P&M, Chapter 2.3-4| HW1 due 27th, HW 2 |
| 1.31 |  LCCDEs, $z$-Transform (ZT): Definition, Existence, ROC.  | Deller, 5:3, 4:1, 4:2; P&M, Chapter 2.4, 3.1 | HW 2 due 3rd |
| 2.7 |  ZT (continued):  Properties, Rational ZT, Pole-Zero Analysis. | Deller, 4:4.2-3; P&M, 3.2-4  | HW 3 |
| 2.14 |  ZT (continued): Inverse ZT, ZT analysis of LTI Systems. | Deller, 4:6, 5:5; P&M, 3.6 | HW 3 due 17th | 
| 2.21 | Midterm and Coding Session | | __Midterm 1 at 2.22__, HW 4 |
| 2.28 | ZT (continued): Inverse ZT, ZT analysis of LTI Systems.  Frequency Analysis: Discrete Time Fourier Series (DTFS), DTF Transform (DTFT): Definition, Convergence, Spectra, Parseval's Theorem  |  Deller,  2:1-2, 2:3.1-2, 2:3.5; P&M, 4.2|  HW 4 due 3rd |
| 3.7 |  __SPRING BREAK__ | |
| 3.14 |  DTFT (continued): Relationship Between $z$-Transform (and CTFT) and DTFT, Frequency Response of LTI Systems|  Deller, 4:3, 5:4.1-2; P&M, 4.3-4  |  HW 5 |
| 3.21 |  DTFT (continued): Frequency Response of LTI Systems, Relationship Between System Function and Freq. Resp., Ideal Filters |  Deller, 5:4.3; P&M, 4.4.2-3, 4.4.5 | HW 5 due 24th, HW 6 |
| 3.28 |  Discrete Fourier Transform (DFT): Definition, Properties, Applications  | Deller, 2:5; P&M, 5.1-2 | HW 6 due 31st, HW 7|
| 4.4 |  Applications of DFT: Block Filtering, Frequency Analysis. Fast FT (In-class coding) | Deller, 2:6; P&M 5.3-4 | __Midterm 2 on 4.7__, HW7 due 7th |
| 4.11 | Machine Learning for Signal Processing: Supervised and Unsupervised Learning, Linear Algebra.  |  |
| 4.18 | MLSP: Linear Regression, Classifiers, Autocorrelation |  |
| 4.25 |  TBD |  |
| 5.2 |  Final's Week |  |