# What is REEDR?
REEDR stands for the **R**esidential **E**nergy **E**fficiency and **D**emand **R**esponse tool. REEDR is an open-source application written in Python that allows you to build, run, and analyze residential EnergyPlus models with relative ease. Some of its key features include:
- ability to run large batches of parametric runs,
- infinite scaling of building envelope and glazing,
- simple inputs for building geometry, infiltration, scheduling, and envelope constructions, and
- automatic aggregation of individual run outputs for easier analysis.

# How to Get REEDR Installed and Running on Your Machine
There are two ways to learn how to install and run REEDR on your machine:
- **Watch how-to videos on YouTube**. There is currently a [Quick Start Guide](https://www.youtube.com/watch?v=5DuCjWeKPXY&t=1s) on YouTube, and there are plans to post more content on how to use REEDR in the future.
- **Keep reading the instructions below**.

To get REEDR running on your machine, you need to install REEDR and a copy of EnergyPlus *v9.5*, the version of EnergyPlus with which REEDR is currently compatible. Note that REEDR currently runs only in Windows environments.

## Installing REEDR
To install REEDR, download *REEDR Setup.exe* from the [latest REEDR release](https://github.com/PtarmiganConsulting/REEDR/releases/tag/v1.0.0-beta) and run it on your machine. *REEDR Setup.exe* is a Windows Installer that will ask where you want REEDR installed.

## Installing EnergyPlus v9.5
To install EnergyPlus v9.5, download a copy from the [EnergyPlus v9.5 github page](https://github.com/NREL/EnergyPlus/releases/tag/v9.5.0) and install it onto your computer using its Windows installer. Remember where you install EnergyPlus on your computer, as you will need to tell REEDR where it is located.

## Running REEDR
There are two main files you need to define and run a REEDR project:
- the *Model Input Template*, and
- *REEDR.exe*.

### The Model Input Template
The *Model Input Template* file is where you define your building models. Specifically, building energy model inputs are defined on the *Model Inputs* tab of this workbook. If you just want to run REEDR, there should already be some example building models defined on the *Model Inputs* tab. (Note that you must *always* make sure you save this file before running REEDR, as REEDR is taking inputs from the saved copy of  the *Model Input Template*, not the live, unsaved version.)

### REEDR.exe
Once you have one or more models defined in the *Model Input Template*, you are ready to define your project details and run REEDR.

To do this, double-click *REEDR.exe* or call it from a command window to launch "a session" of REEDR. You should see two windows open - one is a Python-driven graphical user interface (GUI) where you will define your inputs, and the other is a command window where REEDR will write status updates during the REEDR run.

If it is your first time running REEDR, you must first link up with EnergyPlus (specifically, *energyplus.exe*) on your machine. If you installed EnergyPlus in its default location, REEDR may already have the correct path entered for you. If you did not, you will have to edit the *energyplus.exe* location either manually or using the *Browse* button provided.

Once you've linked up with EnergyPlus, you are ready to define your Project-level inputs and run REEDR. Projec-level inputs include:
- **_Project Name_**: This is a custom string that defines the name of your current project. A folder of this name will hold all REEDR and EnergyPlus output.
- **_Simulation Run Period_**: This is a drop-down menu used to define the length of your simulation. There are three choices: *Annual*, *Sub-Annual* (in which you will need to define your start and end dates in the boxes provided), and *Test Run*. A test run is a diagnostic run that only simulates a single day, and can be used to detect any input errors before running a large batch of models. 
- **_Output Granularity_**: This drop-down menu defines the time period at which output will be generated. The options are *Annual* (available for Annual run periods only), *Hourly*, and *Timestep*. *Timestep* will output at whatever EnergyPlus timestep you have defined in the "Model Input Template".
- **_Output End Uses_**: This drop-down menu defines the subset of energy end uses you wish to output. For *Annual* run periods with *Annual* output, REEDR will automatically generate *All End Uses*, as the amount of data will generally be small. However, for *Hourly* or *Timestep*-level output, file sizes can become very large, so users may wish to select only the end use of interest for the given analysis. 

In addition to the inputs above, there are two radio buttons - one to enable multi-threading, and one to have REEDR ask before overwriting a prior project of the same name.

After you've entered the above information, you can start REEDR by clicking the *Run* button. As REEDR runs, it will output its status and any error messages in the command prompt. REEDR will let you know once a run is completed, and when you can close the current session of REEDR.

## Viewing REEDR Output/Results
In addition to the *Model Input Template* and *REEDR.exe*, the most other common thing you will interact with is the *Projects* folder. The *Projects* folder is where REEDR will store all raw EnergyPlus and processed REEDR output. At the highest level, REEDR creates a folder with the project name provided in the REEDR GUI. Under that, REEDR will create:
- A sub-folder named for each building model with all original EnergyPlus output, and
- A REEDR-generated *Run Report* that aggregates all individual model output and also performs automatic unit conversions, relabeling, and reformatting.

# Credits
REEDR is copyrighted by Ptarmigan Consulting LLC and was developed by [Logan Douglass](https://www.linkedin.com/in/logan-douglass/) and [Christian Douglass](https://www.linkedin.com/in/buildingenergyprofessional/). For all inquiries regarding REEDR, please contact inquiries@ptarmiganconsulting.com.

Significant funding for REEDR was provided by the [Regional Technical Forum (RTF)](https://rtf.nwcouncil.org/). The RTF is a technical advisory committee to the [Northwest Power and Conservation Council](https://www.nwcouncil.org/) established in 1999 to develop standards to verify and evaluate energy efficiency savings.

# License
REEDR is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

REEDR is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with REEDR. If not, see <[https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)>. 