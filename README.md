<div id="top"></div>

<h1 align="center">GPU-Please 🙏</h1>

<!-- TABLE OF CONTENTS -->
* **[About The Project](#about-the-project)**
* **[Getting Started](#getting-started)**
  * [Installation](#installation)
  

<!-- ABOUT -->
## About The Project

Prior to the launch of the NVIDIA 30-Series GPUs (3060, 3070, 3080, 3090) many individuals have been on the hunt to upgrade their PCs–and with the announcement of the 30-Series release, PC owners now had their eyes on the prize. Unfortunately, due to COVID related issues and more importantly online-scalpers the much anticipated GPUs were gone in seconds upon release. Online-scalpers use online bots to purchase large quantities of a product to later sell for aftermarket value. This left many people in shock and angry due to the fact that they had a disadvantage as a regular customer. 

As NVIDIA and other supporting companies continue to try to recover from this, customers are left with the options of buying the GPUs for resell. Sellers have sold the GPUs from anywhere between $500 over retail to 2x the original amount and beyond.

Many customers, including myself, have been following prices for months; hoping that prices would eventually fall. The downside to this is that there is no real way to track prices unless you write them down every time you check. This can become a drag in the long run and can lead to you to eventually give up on finding one for the right price.

GPU-Please is a simple and efficient way to keep track of gpu prices on Amazon. It is as simple as copying and pasting the Amazon links of the GPUs you are interested in to a text file and running the Python script. From there, the script will organize the data and display it in a .csv file sampled below.

#### :chart_with_upwards_trend: Sample Output :chart_with_downwards_trend:

<img src="https://github.com/waPAO/GPU-Please/blob/main/example.png" width="1000" height="500">

Key Features:
* :white_check_mark: Once you input your links, they stay there forever (unless altered) 
* :white_check_mark: The .csv file displays the date and times at which you run the file, making keeping track easier
* :white_check_mark: Everytime you want to update the .csv, all you need to do is rerun the script
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Getting Started -->
## Getting Started

In order to utilize this GPU-Please, please follow the following procedure

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/waPAO/GPU-Please
   ```
2. Install packages ONE at a time (try 'pip3' if 'pip' fails to work)
   ```sh
   pip install requests
   
   pip install beautifulsoup4
   
   pip install datetime
   ```
<p align="right">(<a href="#top">back to top</a>)</p>
