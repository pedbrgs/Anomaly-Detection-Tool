
## Final Project: Anomaly Detection Tool
## "[Visual Pattern Recognition](http://www.dcc.ufmg.br/Pos-graduacao/pesquisa/gruposdet.php?numaut=23)" course (DCC831)<br /> Graduate Program in Computer Science ([PPGCC](http://ppgcc.dcc.ufmg.br/en/)/[UFMG](https://ufmg.br/international-visitors))

**Author:** [Pedro Vinícius A. B. Venâncio](https://www.linkedin.com/in/pedbrgs/)<sup>1,2</sup><br />
**Professor:** [William Robson Schwartz](http://william.dcc.ufmg.br/)<sup>3,4</sup><br />
> <sup>1</sup> Graduate Program in Electrical Engineering (PPGEE/UFMG)<br />
> <sup>2</sup> Gaia, solutions on demand (GAIA)<br />
> <sup>3</sup> Department of Computer Science (DCC/UFMG)<br />
> <sup>4</sup> Smart Sense Laboratory (SENSE/UFMG)

***

### About

This repository contains the source code for the Final Project of "Visual Pattern Recognition" course (DCC831). The code was implemented in Python 3.6.8 using computer vision libraries such as OpenCV 4.1.0 and Torch 1.3.0.

***

### Problem description

Implement a method that, given an input image like those shown in Figure 1, detects anomalous regions ([Instructions in Portuguese](https://github.com/pedbrgs/anomaly-detection-tool/blob/master/Instructions-PT.pdf)).
<figure>
  <p align="center">
  <img src="https://i.ibb.co/wKCFnRq/img1-1.jpg" width="320"/> <img src="https://i.ibb.co/HgHhpCv/img5-1.jpg" width="320"/> 
  <figcaption><p align="center">Figure 1: Examples of input images.</p></figcaption>
  </p>
</figure>

***

### Proposed approach

The proposed solution is shown in the following figures. The edges of all patterns are identified in the grayscale image by morphological filtering (erosion).

<figure>
  <p align="center">
    <img src="https://i.ibb.co/L5BjPkK/process.png" width="35%">
    <figcaption><p align="center">Figure 2: Object segmentation through morphological filtering.</p></figcaption>
  </p>
</figure>

Each pattern is passed through the feature extractor and generates a feature vector (dimensionality reduction).

<figure>
  <p align="center">
    <img src="https://i.ibb.co/pPhLj0h/Resnet34-Modified.png" width="85%">
    <figcaption><p align="center">Figure 3: Feature extractor based on <a href="https://arxiv.org/pdf/1512.03385.pdf">ResNet-34</a>.</p></figcaption>
  </p>
</figure>

The difference between the feature vectors of two patterns is calculated through the cosine similarity:

<p align="center">
<img src="https://latex.codecogs.com/svg.latex?\large&space;\text{similarity}(\mathbf{A},\mathbf{B})=\frac{\mathbf{A}\mathbf{\cdot}\mathbf{B}}{||\mathbf{A}||||\mathbf{B}||}=\frac{\sum_{i=1}^{n}A_iB_i}{\sqrt{\sum_{i=1}^{n}A_i^2}\sqrt{\sum_{i=1}^{n}B_i^2}}" title="cosine similarity" />
</p>

where n is the number of features (vector size). The pattern that most differs from the others is the anomalous pattern (lowest sum of cosine similarities).

***

### Running code

To run this detector on an input image, just type the command:

`python3 detector.py --data data/<input image>`

Make sure you are in the same directory as the main code `detector.py` and the path to input image is correct.

***

### Results

The results for the examples in Figure 1 are shown below. Anomalies are marked by a bounding box.

<figure>
  <p align="center">
  <img src="https://i.ibb.co/9qQMMhb/img1.jpg" width="320"/> <img src="https://i.ibb.co/F86jcy7/img5.jpg" width="320"/> 
  <figcaption><p align="center">Figure 4: Examples of output images.</p></figcaption>
  </p>
</figure>

For more results, go to the [`results/`](https://github.com/pedbrgs/Anomaly-Detection-Tool/tree/master/results) directory.

***

### Citation Info

If you're using these codes in any way, please let them know your source:

```
@Misc{Venancio2019-ADT,
title = {Anomaly Detection Tool},
author = {Pedro Vinicius A. B. Venancio},
howPublished = {\url{https://git.io/JTBZM}},
year = {2019}}
```

***

### Contact

Please send any bug reports, questions or suggestions directly in the repository.
