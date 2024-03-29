# Dekimashita

![Version](https://img.shields.io/badge/version-0.0.3-green.svg?cacheSeconds=2592000)
![ProjectImage](https://raw.githubusercontent.com/ryyos/ryyos/main/images/Dekimashita/photo_2024-01-31_09-37-59.jpg)

**a library containing a collection of utility functions designed to filter and process text data based on certain criteria. These functions are useful for various text processing tasks, such as removing unwanted characters, extracting specific information, or cleaning input data.**

## Features ✨

- **Alphabetic Filtering**: Easily filter out non-alphabetic characters from text data.
- **Numeric Filtering**: Quickly remove non-numeric characters from text strings.
- **Alphanumeric Filtering**: Filter text to retain only alphanumeric characters, excluding special symbols.
- **Customization**: Ability to customize the filtering criteria based on specific requirements.
- **TextCleaning**: Cleanse input text from unwanted characters to prepare it for further processing or analysis.
- **Normalization**: Standardize text data by removing irregular characters or symbols

## Requirement ⚙️

- [Python](https://www.python.org/) v3.11.6+

## Installation 🛠️

```sh
pip install dekimashita
```

## How To Usage 🤔

#### 1. Dekimashita.vdict(data, [chars])

    Filter dictionary values recursively, ignoring specified characters.

    Args:
        data (dict or list): Data (dictionary or list containing dictionaries) to filter.
        chars (list): List of characters to filter.

    Returns:
        dict or list: Filtered data.

### ⚠️ Sample ⚠️

```python
data = {
  "university": {
    "name": "Example University",
    "location": "City XYZ",
    "courses": [
      {
        "course_id": "CS101",
        "title": "Introduction \n to \n Computer \n\n Science",
        "lecturer": {
          "name": "Dr. Alan\n Smith",
          "email": "alan.smith@example.com",
          "office": {
            "building": "Engineering Tower",
            "room_number": "123"
          }
        },
        "students": {
            "name": "John Doe",
            "student_id": "123456",
            "email": "john.doe@example.com",
            "grades": {
              "assignments": [
                {
                  "assignment_id": "001",
                  "score": 95,
                  "comments": "Great job on the assignment!\nKeep up the good work."
                },
                {
                  "assignment_id": "002",
                  "score": 85,
                  "comments": "Your\n effort is commendable.\r\r However,\nthere is room"
                }
              ],
              "final_exam": {
                "score": 88,
                "comments": "Solid \nperformance overall.\n\rYour understanding of the subject"
              }
            }
          }
      }
    ]
  }
}
```

<br>

#### without Dekimashita filter

```python
import json

data = # data_sample

with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
```

#### If you have a very complex dictionary and you write without using the Dekimashita filter you will get results like this

<br>
<div style="text-align: center;">
  <img src="https://raw.githubusercontent.com/ryyos/ryyos/main/images/Dekimashita/nopng.png"> 
</div>
<br>

#### with Dekimashita filter

```python
import json
from dekimashita import Dekimashita

data = # data_sample
clear = Dekimashita.vdict(data, ['\n', '\r'])

with open("data.json", "w") as json_file:
    json.dump(clear, json_file, indent=4)
```

#### By using the Dekimashita filter you get a clean dictionary like this

<br>
<div style="text-align: center;">
  <img src="https://raw.githubusercontent.com/ryyos/ryyos/main/images/Dekimashita/yeee.png"> 
</div>
<br>

#### 2. Dekimashita.vspace(text)

    Remove extra spaces from text.

    Args:
        text (str): Input text.

    Returns:
        str: Text with extra spaces removed.

### sample

```python
from dekimashita import Dekimashita

text = 'moon   beautiful   isn"t   it'

clear = Dekimashita.vspace(text)

print('without Dekimashita filter: '+ text)
print('with Dekimashita filter: ' + clear)
```

```
# output

without Dekimashita filter: moon   beautiful   isn"t   it
with Dekimashita filter: moon beautiful isn"t it
```

#### 3. Dekimashita.valpha(text)

    Remove non-alphabetic characters (except a-z, A-Z) from text.

    Args:
      text (str): Input text.

    Returns:
      str: Filtered text containing only alphabetic characters.

### sample

```python
from dekimashita import Dekimashita

text = 'mo&on b)(*&^%$e!au!t@#$i*f!ul is!!$#n"t i)(*&^t'

clear = Dekimashita.valpha(text)

print('without Dekimashita filter: '+ text)
print('with Dekimashita filter: ' + clear)
```

```
# output

without Dekimashita filter: mo&on b)(*&^%$e!au!t@#$i*f!ul is!!$#n"t i)(*&^t
with Dekimashita filter: moon beautiful isnt it
```

#### 4. Dekimashita.vnum(text)

    Remove non-numeric characters from text.

    Args:
      text (str): Input text.

    Returns:
      str: Filtered text containing only numeric characters.

### sample

```python
from dekimashita import Dekimashita

text = ' mo30on be7aut20iful i05sn"t it'

clear = Dekimashita.vnum(text)

print('without Dekimashita filter: '+ text)
print('with Dekimashita filter: ' + clear)

```

```
# output

without Dekimashita filter:  mo30on be7aut20iful i05sn"t it
with Dekimashita filter: 3072005
```

#### 5. Dekimashita.vtext(text)

    Remove non-alphanumeric characters (except a-z, A-Z, 0-9) from text.
      Double spaces are replaced with a single space.

    Args:
      text (str): Input text.

    Returns:
      str: Filtered text containing only alphanumeric characters.

### sample

```python
from dekimashita import Dekimashita

text = 'moon \t\t bea^%$#@utiful isn"t it 30705'

clear = Dekimashita.vtext(text)

print('without Dekimashita filter: '+ text)
print('with Dekimashita filter: ' + clear)

```

```
# output

without Dekimashita filter: moon                 bea^%$#@utiful isn"t it 30705
with Dekimashita filter: moon beautiful isnt it 30705
```

#### 6. Dekimashita.vdir(text, separator)

    """
    Remove non-alphanumeric characters (except a-z, A-Z, 0-9) from text.
    Convert all letters to lowercase. Replace spaces with a specified separator.
    Double separators are replaced with a single separator.

    Args:
      text (str): Input text.
      separator (str): Separator to replace spaces (default is '_').

    Returns:
      str: Filtered and normalized text.
    """

### sample

```python
from dekimashita import Dekimashita

text = 'Moon Beautiful Isn"t It'

clear = Dekimashita.vdir(text)

print('without Dekimashita filter: '+ text)
print('with Dekimashita filter: ' + clear)
```

```
# output

without Dekimashita filter: Moon Beautiful Isn"t It
with Dekimashita filter: moon_beautiful_isnt_it
```

## 🚀Structure

```
│   LICENSE
│   README.md
│   setup.py
│
└───dekimashita
        dekimashita.py
        __init__.py
```

## Author

👤 **Rio Dwi Saputra**

- Twitter: [@ryyo_cs](https://twitter.com/ryyo_cs)
- Github: [@ryyos](https://github.com/ryyos)
- Instagram: [@ryyo.cs](https://www.instagram.com/ryyo.cs/)
- LinkedIn: [@rio-dwi-saputra-23560b287](https://www.linkedin.com/in/rio-dwi-saputra-23560b287/)

<a href="https://www.linkedin.com/in/rio-dwi-saputra-23560b287/">
  <img align="left" alt="Ryo's LinkedIn" width="24px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
</a>
<a href="https://www.instagram.com/ryyo.cs/">
  <img align="left" alt="Ryo's Instagram" width="24px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" />
</a>
