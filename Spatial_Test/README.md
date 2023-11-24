# SpatialReasoning_Jupyter
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