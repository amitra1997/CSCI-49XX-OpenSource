## Part 1

### 1. Submitty
(https://github.com/Submitty/Submitty)

Submitty is RPI's open source program assignment submission system.

Evaluation Factor | Level (0-2) | Evaluation Data 
|:-|:-:|:-|
| **Licensing** | 2 | Submitty uses the BSD 3-Clause License, which is approved by the OSI |
| **Language** | 1 | 1. PHP: 32.2% :: 2. HTML: 22.8% :: 3. JavaScript: 15.3% |
| **Level of Activity** | 2 | All 4 quarters in the last year were active |
| **Number of Contributors** | 2 | Submitty has 69 contributors |
| **Product Size** | 2 | Submitty is 36.52 MB | 
| **Issue Tracker** | 2 | Issues are actively being added and resolved |
| **New Contributor** | 2 | There is a "How to Contribute" page present with information on coding style, commits, reviewing and submitting pull requests, and edit the codebase. Instructions to download and install are present, as well as a link to the Submitty slack channel. The README also contains basic information about the project, features, and motivations. Developer documentation is pretty extensive. https://submitty.org/developer/how_to_contribute |
| **Community Norms** | 1 | There is no Code of Conduct. Communication is primarily handled through Slack, which does not contain rude or inappropriate behavior. Communication is not as frequent as expected, given the size of the project. The community seems to primarily communicate through issues and requests on git, rather than through Slack. |
| **User Base** | 2 | The user base is RPI students taking coding classes, and their corresponding Professors/TAs who post and grade those homeworks with the assistance of Submitty. The instructions to download and utilize the software are clear and easy to access. Use of the software is also easy to find and understand. |
| **Total Score** | - | 16 |

### 2. YACS
(https://github.com/YACS-RCOS/yacs)

YACS is RPI's open source class scheduling system.

Evaluation Factor | Level (0-2) | Evaluation Data 
|:-|:-:|:-|
| **Licensing** | 2 | YACS uses the GNU Affero General Public License, which is approved by the OSI |
| **Language** | 1 | 1. Ruby: 51.9% :: 2. TypeScript: 16.8% :: 3. JavaScript: 11.1% |
| **Level of Activity** | 2 | All 4 quarters in the last year were active |
| **Number of Contributors** | 2 | YACS has 31 contributors |
| **Product Size** | 2 | YACS is 19.22 MB | 
| **Issue Tracker** | 2 | Issues are actively being added and resolved |
| **New Contributor** | 1 | There is a "Setup Guide" page present with information on installing, setting up and running Submitty. https://yacs.io/#/contributors/setup_guide Communication mechanisms may exist, however I was unable to find them after a long search. Additionally, I was unable to find a discussion platform for the project. There is a nice getting started page for new users to be able to jump in and contribute with ease, however. https://yacs.io/#/contributors/getting_started |
| **Community Norms** | 1 | There is a Code of Conduct, which includes no discrimination on the basis of sex, race, or otherwise uncontrollable characteristics. Welcoming and encouraging new developers is emphasized in the CoC. Finally, avenues to report and correct unacceptable behaviors are readily available. Communication is primarily handled through git, which does not contain rude or inappropriate behavior. Beyond that, there does not seem to be communication avenues such as Slack that are easily accessible and available to users, unless users have access to the official RCOS slack. |
| **User Base** | 2 | The user base is RPI students looking to schedule courses. One thing to note is that users do not use this often, but rather only about twice a year when forming schedules for the upcoming academic semester. Given the clunky and hard-to-use design of RPI's SIS scheduling, this tool is greatly appreciated and utilized by nearly the entire student body to form and compare schedules. The instructions to download and utilize the software are clear and easy to access. Use of the software is also easy to find and understand. |
| **Total Score** | - | 15 |

### 3. Chromium
(https://chromium.googlesource.com/chromium/src)
Official github mirror: (https://github.com/chromium/chromium)

Chromium is a lightweight web browser utilizing sandbox security. 

Evaluation Factor | Level (0-2) | Evaluation Data 
|:-|:-:|:-|
| **Licensing** | 2 | Chromium uses the BSD 3-Clause License, which is approved by the OSI |
| **Language** | 2 | 1. C++ :: 2. Webcore :: 3. JavaScript (Percentages not available due to extremely large codebase size) |
| **Level of Activity** | 2 | All 4 quarters in the last year were active |
| **Number of Contributors** | 2 | Chromium has an infinite symbol for number of contributors (too many to display) |
| **Product Size** | 1 | Chromium is 12.15 GB, far too large for my purposes and understanding within the scope of this class | 
| **Issue Tracker** | 2 | Issues are actively being added and resolved |
| **New Contributor** | 2 | https://www.chromium.org/developers This page contains everything needed for new developers, including downloading and installing the environment, learning and getting around the codebase, communication mechanisms and discussion groups, and the Web presence.  |
| **Community Norms** | 2 | There is a Code of Conduct, which begins by informing users to be respectful and constructive. https://www.chromium.org/conduct Harassment is defined clearly and concisely. Finally, avenues to report and correct unacceptable behaviors are readily available, along with information on consequences of failing to comply with the CoC. Communication is primarily handled through discussion groups, which does not contain rude or inappropriate behavior. |
| **User Base** | 2 | The user base is everyone looking to use a fast, lightweight and secure web browser. The instructions to download and utilize the software are clear and easy to access. Use of the software is also easy to find and understand. |
| **Total Score** | - | 17 |
 
## Part 2
In this section I further analyze Submitty.

#### Goal
Submitty strives to build a homework submission, automated grading and TA/instructor grading system. 

#### Significance
Submitty is one of the most impactful open source projects on campus at RPI. Every student who takes a computer science course with code homework submission uses it to quickly and reliably submit homework assignments for grading. TAs and Professors depend on the software to automatically grade these assignments accurately when applicable, while also screening all assignments for plagiarism. It saves students and TAs/Professors hours of work in hand grading. It provides an easy way to submit homework, with quick and automated feedback to avoid unnecessary confusion. Submitty's importance to the computer science department at Rensselaer can not be emphasized enough.

#### Licensing
Submitty is licensed under the BSD 3-Clause License, or the "New BSD License" or "Modified BSD License". This is approved by the Open Source Initiative because it allows for free use, modification and sharing, given certain conditions are met. Redistribution of the code is permitted, so long as the copyright notice is maintained. Sharing is also permitted, however promotion of products derived from the software may not reference the copyright holder or contributors without prior written consent from the copyright holder. This license is perfect for Submitty, yielding it a rank of 2. 

https://github.com/Submitty/Submitty/blob/master/LICENSE.md

#### Language
Submitty is primarily written in five languages: PHP, HTML, JavaScript, Python and C++. PHP, HTML, and JavaScript drive the UI and web interface, while Python and C++ drive the underlying algorithms and code. There is also some Shell present, although minimally (~2.5%). The front end allows for running without any installation of Adobe Flash necessary. I have not written extensively in PHP, although I have extensive experience in Python, C++, HTML and Javascript. Therefore, as PHP makes up ~30% of Submitty, while the other primary languages together account for ~65%, I have scored it with 1.

https://github.com/Submitty/Submitty/search?l=php

#### Level of Activity
Submitty has been in active development for a long time. In fact, it has been in development for so long that I am unable to view insights for the repository creation date. It has nearly 426,000 lines of code. For as far back as I can access, there has been active development on a weekly and even daily basis. On July 15, 2018 there were 46 commits, the high for 2018. Given the high levels of activity for every accessible quarter of development, I have scored this section with 2.

https://github.com/Submitty/Submitty/graphs/commit-activity

#### Number of Contributors
Submitty has 69 contributors. According to the foss2serve rubric, that alone gives it a score of 2. Most contributors are RPI students. Barbara Cutler is in charge of the project, and is the primary contributor.

#### Product Size
Submitty is 36.52 MB in size. This is a decently sized project, and perfect for the scope of this class. The codebase is not so large that it will take a very long time to understand, yet substantial enough to be a strongly impactful project. Therefore, I scored this section with 2.

#### Issue Tracker
There are 334 open issues present on Submitty. 1,163 issues have been closed in the past. These are present on Github Issues. Most issues have posts from contributors outlining potential solutions. There is a provided template for contributing issues, along with useful "tags" that can be added to categorize them. With constant monitoring from contributors and relatively quick resolutions for most issues, I scored this section with 2. 

https://github.com/Submitty/Submitty/issues

#### New Contributor
Submitty contains instructions on getting the software up and running. There is also a "How to Contribute" page, with easy to follow guidelines for getting started. There is a coding style guide, describing guidelines for each of the coding languages in Submitty. Information on every facet of Submitty, from the Rainbow Grading to the Interface Design, is accessible on the developer page, which makes it simple for new developers to get involved, understand the codebase quickly and efficiently, and begin contributing. There is a tutorial on sending in error reports. There is also a dedicated communication channel through the RCOS Slack, for communication among developers. All these tools make Submitty very welcoming to new developers and other contributors, giving it a score of 2 in this section.

https://submitty.org/developer/how_to_contribute

https://submitty.org/developer/coding_style_guide

https://submitty.org/developer

#### Community Norms
One issue with this open source project is the lack of a Code of Conduct. Although RCOS has a general Code of Conduct for all projects within its scope, Submitty does not reference it anywhere publicly. This is not necessarily a huge issue, but can potentially become one with a developer base as large as Submitty's. While there is no CoC present, there does not seem to be any rude or inappropriate behavior on the Slack channel, issue tracker, or otherwise. Communication is not as frequent as I expected for a project of this size, but seems to occur when necessary. Additionally, development and communication seems to peak in the winter months, and fall off in the Spring. Finally, there is a public forum for questions, and links to directly contact the development team.

https://groups.google.com/forum/#!forum/submitty

##### Development Team
submitty@cs.rpi.edu
submitty-admin@googlegroups.com

#### User Base
Submitty's user base consists of nearly the entire RPI Computer Science department. All Professors/TAs assigning work do so through Submitty for coding assignments. Students rely on it for automated homework grading, grade tracking and feedback. Given that computer science is the largest single major declared on RPI's campus, Submitty's scope of usage is very large.

#### Personal Appeal
Although Submitty did not score as highly as Chromium when using the foss2serve rubric, I still found it to be the most appealing project. There are certain categories I value far more than others, such as scope of the project (project size) and personal affinity to the project (user base), even though on the foss2serve rubric all categories are ranked equally from 0 to 2. I would like to contribute to a project in a way where I can make a significant impact, to a user base that I care about. Submitty offers that solution. While the language it is written in may not be ideal for my purposes, I have confidence that I can quickly learn and adapt. 