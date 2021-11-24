# Hier ein paar Beispiele zum selbst überlegen

Versuch dich selbst an einem der Beispiele. Wie sieht deine Lösung aus?

## Bücher
```plantuml
@startuml
scale 1.5
class Book {
title: str
author: Author
chapters: [Chapters]
isbn: str
}

class Chapter {
order_nr: int
title: str
text: str
}

class Author {
firstname: str
lastname: str

}

Book "n" -- "n" Author
Book "1" -- "n" Chapter
@enduml
```

## Vokabeltrainer
````plantuml
@startuml
scale 3
class Dictionary {
language_name: str
words: [Word]
}

class Word {
word: str
translated_word: str
check_translated_word(translated_word: str)
}
Dictionary "n" -- "n" Word
@enduml
````

## Autos

```plantuml
@startuml
scale 1.5
class Vehicle {
speed: int
horsepower: int
drive()
stop()
honk()
}

class Car {
seats: int
}

class Truck {
seats: int
maximum_load: int
}

Vehicle <|-- Car
Vehicle <|-- Truck
@enduml
```

## Tamagotchi

```plantuml
@startuml
scale 1.5

class Tamagotchi {
hunger: int
boredom: int
words: [str]
clock_tick()
feed()
teach()
hi()
reduce_boredom()
}
@enduml
```