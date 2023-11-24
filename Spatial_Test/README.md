# SpatialReasoning_Jupyter

English:
This application creates a spatial reasoning test. In the application, the user becomes familiar with the instructions, enters data, and solves five puzzles. Then the results are displayed, which are also saved in the cloud through the API to Google Sheets.

The application aims to:

- Create a simple GUI in a Jupyter notebook.
- Collect user data - personal and related to the time spent on puzzles.
- Produce puzzles live, not from photos.
Written in object-oriented programming, the app is divided into several classes: 
DataSaver - Manages the collection and storage of data. It gathers responses and other user information, then sends this data to a Google Sheets document.

Timer - Manages the temporal aspects of the spatial reasoning task. It tracks how much time users spend on individual puzzles and on the entire task, and manages time limits.

WindowManager - Controls the display of different windows in the user interface. Manages transitions between different task panels, such as starting the test, entering authentication data, showing puzzles, and ending the test.

Panels - Responsible for creating and managing the various panels (user interface sections) displayed during the task. Each panel performs a specific function, such as welcoming participants, collecting authentication data, displaying puzzles, and showing the final message.

PuzzleCreator - Generates puzzles for the spatial reasoning task. It contains the logic for creating various 3D puzzles and their 2D counterparts.

Each class cooperates to provide an interactive and functional user experience during the task, from the beginning of the test to the final submission of responses and display of results. The classes are sorted quite randomly, but in such a way as to more or less allow easy tracking of threads.

PROBLEM: The whole program works, but it has one flaw: if the user, stressed by time pressure, starts spamming the choice buttons A, B, C, D defined in the Panels class, method self.puzzle_panel, it will record an answer for a single puzzle several times. I tried disabling the button immediately after clicking, unsuccessfully. However, I have not tried using a flag that would disable the function. My suspicion is that the button does indeed turn off, but "after the fact", inside the function performing the task and after it has been clicked. Perhaps, therefore, the message about disabling the button is never returned from the function that handles the consequences of clicking the button.

____________________________________________________

Polish:
ta aplikacja tworzy test na zdolności przestrzennego rozumowania
w aplikacji użytkownik zapoznaje się z instrukcjami, wprowadza dane i rozwiązuje pięć łamigłówek.
potem wyświetlają się wyniki, które zostają też zapisane w chmurze przez API do google sheets.

Aplikacja ma na celu:
- wytworzyć prosty GUI w jupyter notebook
- zbierać dane od użytkownika - personalne i dotyczące czasu spędzonego na układankach
- wyprodukować układanki na żywo, nie ze zdjęć

Napisana w object-oriented programming, apka podzielona jest na kilka klas: 
DataSaver - Zarządza zbieraniem i przechowywaniem danych. Gromadzi odpowiedzi i inne informacje o użytkowniku, a następnie wysyła te dane do dokumentu Google Sheets.

Timer - Zarządza aspektami czasowymi zadania z rozumowaniem przestrzennym. Śledzi, ile czasu użytkownicy spędzają na poszczególnych łamigłówkach i na całym zadaniu, oraz zarządza limitami czasu.

WindowManager - Kontroluje wyświetlanie różnych okien w interfejsie użytkownika. Zarządza przejściami między różnymi panelami zadania, takimi jak rozpoczęcie testu, wprowadzanie danych uwierzytelniających, pokazywanie łamigłówek i zakończenie testu.

Panels - Odpowiedzialna za tworzenie i zarządzanie różnymi panelami (sekcjami interfejsu użytkownika) wyświetlanymi podczas zadania. Każdy panel pełni określoną funkcję, taką jak powitanie uczestników, zbieranie danych uwierzytelniających, wyświetlanie łamigłówek i pokazywanie komunikatu końcowego.

PuzzleCreator - Generuje łamigłówki do zadania z rozumowaniem przestrzennym. Zawiera logikę tworzenia różnych łamigłówek 3D i ich odpowiedników 2D.

Każda klasa współpracuje, aby zapewnić interaktywne i funkcjonalne doświadczenie użytkownika podczas zadania, od początku testu do końcowego przesłania odpowiedzi i wyświetlenia wyników.
Klasy posortowane są dość przypadkowo, jednak tak żeby mniej więcej umożliwić proste śledzenie wątków

PROBLEM:
cały program działa, ale ma jedną wadę: jeśli użytkownik, zestresowany presją czasu, zacznie spamować przyciski wyboru A,B,C,D zdefiniowane w klasie Panels, metodzie self.puzzle_panel, 
to zapisze kilkanaście razy odpowiedź za jedną układankę. Próbowałem wyłączać przycisk natychmiast po kliknięciu, bezskutecznie. Nie spróbowałem natomiast używania flagi
która wyłączałaby funkcę. Moje podejrzenie jest takie że przycisk co prawda wyłącza się, ale "po fakcie", wewnątrz funkcji wykonującej zadanie i gdy już został kliknięty. 
Być może więc komunikat o wyłączeniu przycisku nigdy nie zostaje zwrócony od funkcji, która obsługuje następstwa klikania w przycisk.