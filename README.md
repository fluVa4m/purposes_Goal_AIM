<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Unlicense License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]




![Uploading readme-banner-pyqt6-ref_copy.svg…]()
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 640" width="1280" height="640">
  <defs>
    <!-- Тень для окон -->
    <filter id="winShadow" x="-10%" y="-10%" width="125%" height="125%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.14"/>
    </filter>
    <!-- Градиент логотипа -->
    <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4F46E5" />
      <stop offset="100%" stop-color="#7C3AED" />
    </linearGradient>
    <linearGradient id="checkGrad" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10B981" />
      <stop offset="100%" stop-color="#34D399" />
    </linearGradient>
    <!-- Сетка на фоне -->
    <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#E2E8F0" stroke-width="1"/>
    </pattern>
  </defs>

  <!-- Базовый фон в светлой нативной палитре Windows / Qt -->
  <rect width="1280" height="640" fill="#F1F5F9" />
  <rect width="1280" height="640" fill="url(#grid)" opacity="0.65" />

  <!-- ЛЕВАЯ ЧАСТЬ: БРЕНДИНГ ПРОЕКТА -->
  <g transform="translate(56, 75)">
    <!-- Бейдж PyQt6 -->
    <rect x="0" y="0" width="174" height="32" rx="4" fill="#E6F4EA" stroke="#34A853" stroke-width="1"/>
    <circle cx="16" cy="16" r="5" fill="#41CD52"/>
    <text x="30" y="21" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="600" fill="#1E4620">Built with PyQt6</text>

    <!-- Логотип -->
    <g transform="translate(0, 56)">
      <rect x="0" y="0" width="96" height="96" rx="22" fill="url(#logoGrad)" />
      <rect x="28" y="18" width="40" height="5" rx="2.5" fill="#FFFFFF" />
      <rect x="28" y="73" width="40" height="5" rx="2.5" fill="#FFFFFF" />
      <path d="M 33 23 C 33 38, 48 44, 48 48 C 48 52, 33 58, 33 73 L 63 73 C 63 58, 48 52, 48 48 C 48 44, 63 38, 63 23 Z" 
            fill="none" stroke="#FFFFFF" stroke-width="3.5" stroke-linejoin="round" />
      <path d="M 37 69 C 40 62, 45 60, 48 60 C 51 60, 56 62, 59 69 Z" fill="#A5B4FC" />
      <circle cx="68" cy="68" r="14" fill="#1E1B4B" />
      <path d="M 62 68 L 66 72 L 75 63" fill="none" stroke="url(#checkGrad)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
    </g>

    <!-- Заголовок и подзаголовок -->
    <text x="0" y="205" font-family="'Segoe UI', Arial, sans-serif" font-size="44" font-weight="700" fill="#0F172A">Deadline Planner</text>
    <text x="0" y="242" font-family="'Segoe UI', Arial, sans-serif" font-size="18" fill="#475569">Нативный трекер целей, дедлайнов</text>
    <text x="0" y="268" font-family="'Segoe UI', Arial, sans-serif" font-size="18" fill="#475569">и визуальной статистики на Python</text>

    <!-- Разделитель как QFrame -->
    <line x1="0" y1="296" x2="360" y2="296" stroke="#CBD5E1" stroke-width="1"/>

    <!-- Системные плашки стека (Python 3.9+, PyQt6, QtWidgets) -->
    <g transform="translate(0, 322)" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#1E293B">
      <rect x="0" y="0" width="112" height="32" rx="3" fill="#E1E1E1" stroke="#ADADAD" stroke-width="1"/>
      <text x="56" y="21" text-anchor="middle" font-weight="600">Python 3.9+</text>

      <rect x="122" y="0" width="76" height="32" rx="3" fill="#E1E1E1" stroke="#ADADAD" stroke-width="1"/>
      <text x="160" y="21" text-anchor="middle">PyQt6</text>

      <rect x="208" y="0" width="108" height="32" rx="3" fill="#E1E1E1" stroke="#ADADAD" stroke-width="1"/>
      <text x="262" y="21" text-anchor="middle">QTabWidget</text>

      <rect x="0" y="42" width="124" height="32" rx="3" fill="#E1E1E1" stroke="#ADADAD" stroke-width="1"/>
      <text x="62" y="63" text-anchor="middle">QProgressBar</text>

      <rect x="134" y="42" width="116" height="32" rx="3" fill="#E1E1E1" stroke="#ADADAD" stroke-width="1"/>
      <text x="192" y="63" text-anchor="middle">QListWidget</text>
    </g>

    <!-- Нижняя подпись -->
    <text x="0" y="455" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="#64748B">Легкий десктопный интерфейс без тяжелых зависимостей</text>
  </g>

  <!-- ПРАВАЯ ЧАСТЬ: ДВА ОКНА ПО РЕФЕРЕНСУ СКРИНШОТОВ -->

  <!-- ЗАДНЕЕ ОКНО (Вкладка «статистика» как на 1-м скриншоте) -->
  <g transform="translate(835, 78)" filter="url(#winShadow)">
    <rect x="0" y="0" width="390" height="495" fill="#F0F0F0" stroke="#707070" stroke-width="1"/>
    <rect x="1" y="1" width="388" height="30" fill="#FFFFFF"/>
    <rect x="10" y="8" width="14" height="14" rx="3" fill="#3B82F6"/>
    <path d="M 13 15 L 16 18 L 21 12" fill="none" stroke="#FFFFFF" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
    <text x="32" y="20" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#000000">мои цели</text>
    <g stroke="#000000" stroke-width="1" fill="none">
      <line x1="302" y1="15" x2="312" y2="15"/>
      <rect x="336" y="10" width="10" height="10"/>
      <line x1="368" y1="10" x2="378" y2="20"/>
      <line x1="378" y1="10" x2="368" y2="20"/>
    </g>

    <rect x="1" y="31" width="388" height="24" fill="#FFFFFF"/>
    <text x="12" y="47" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#000000">файл</text>
    <text x="52" y="47" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#000000">справка</text>

    <rect x="12" y="64" width="44" height="44" rx="10" fill="#3B82F6"/>
    <path d="M 23 86 L 31 94 L 45 78" fill="none" stroke="#FFFFFF" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
    <text x="66" y="94" font-family="'Segoe UI', Arial, sans-serif" font-size="22" fill="#000000">мои цели</text>

    <g transform="translate(12, 118)" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#000000">
      <rect x="0" y="3" width="48" height="23" fill="#E1E1E1" stroke="#ADADAD" stroke-width="1"/>
      <text x="24" y="18" text-anchor="middle">цели</text>
      <rect x="48" y="0" width="84" height="26" fill="#FFFFFF" stroke="#ADADAD" stroke-width="1"/>
      <text x="90" y="17" text-anchor="middle">статистика</text>
      <rect x="132" y="3" width="76" height="23" fill="#E1E1E1" stroke="#ADADAD" stroke-width="1"/>
      <text x="170" y="18" text-anchor="middle">создание</text>
    </g>

    <rect x="12" y="143" width="366" height="324" fill="#FFFFFF" stroke="#ADADAD" stroke-width="1"/>
    <line x1="61" y1="143" x2="143" y2="143" stroke="#FFFFFF" stroke-width="2"/>

    <text x="195" y="172" text-anchor="middle" font-family="'Segoe UI', Arial, sans-serif" font-size="14" font-weight="700" fill="#000000">всего: 3   выполнено: 2   (67%)</text>

    <rect x="24" y="184" width="312" height="24" fill="#E6E6E6" stroke="#BCBCBC" stroke-width="1"/>
    <rect x="25" y="185" width="208" height="22" fill="#06B025"/>
    <text x="342" y="201" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#000000">67%</text>

    <text x="195" y="242" text-anchor="middle" font-family="'Segoe UI', Arial, sans-serif" font-size="14" font-weight="700" fill="#000000">статистика</text>

    <rect x="92" y="275" width="20" height="145" fill="#4CAF50"/>
    <rect x="188" y="348" width="20" height="72" fill="#E57373"/>
    <line x1="60" y1="420" x2="335" y2="420" stroke="#9E9E9E" stroke-width="1.5"/>
    <text x="102" y="440" text-anchor="middle" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#000000">каждый день</text>
    <text x="198" y="440" text-anchor="middle" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#000000">на месяц</text>
    <text x="292" y="440" text-anchor="middle" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#000000">долгосрочные</text>

    <rect x="1" y="472" width="388" height="22" fill="#F0F0F0"/>
    <text x="10" y="487" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="#000000">целей: 3, выполнено: 2</text>
    <path d="M 382 492 L 387 487 M 378 492 L 387 483 M 374 492 L 387 479" stroke="#888888" stroke-width="1"/>
  </g>

  <!-- ПЕРЕДНЕЕ ОКНО (Вкладка «цели» со списком как на 2-м скриншоте) -->
  <g transform="translate(465, 42)" filter="url(#winShadow)">
    <rect x="0" y="0" width="420" height="535" fill="#F0F0F0" stroke="#707070" stroke-width="1"/>
    <rect x="1" y="1" width="418" height="30" fill="#FFFFFF"/>
    <rect x="10" y="8" width="14" height="14" rx="3" fill="#3B82F6"/>
    <path d="M 13 15 L 16 18 L 21 12" fill="none" stroke="#FFFFFF" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
    <text x="32" y="20" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#000000">мои цели</text>
    <g stroke="#000000" stroke-width="1" fill="none">
      <line x1="332" y1="15" x2="342" y2="15"/>
      <rect x="366" y="10" width="10" height="10"/>
      <line x1="398" y1="10" x2="408" y2="20"/>
      <line x1="408" y1="10" x2="398" y2="20"/>
    </g>

    <rect x="1" y="31" width="418" height="24" fill="#FFFFFF"/>
    <text x="12" y="47" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#000000">файл</text>
    <text x="52" y="47" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#000000">справка</text>

    <rect x="12" y="64" width="44" height="44" rx="10" fill="#3B82F6"/>
    <path d="M 23 86 L 31 94 L 45 78" fill="none" stroke="#FFFFFF" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
    <text x="66" y="94" font-family="'Segoe UI', Arial, sans-serif" font-size="22" fill="#000000">мои цели</text>

    <g transform="translate(12, 118)" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#000000">
      <rect x="0" y="0" width="52" height="26" fill="#FFFFFF" stroke="#ADADAD" stroke-width="1"/>
      <text x="26" y="17" text-anchor="middle">цели</text>
      <rect x="52" y="3" width="84" height="23" fill="#E1E1E1" stroke="#ADADAD" stroke-width="1"/>
      <text x="94" y="18" text-anchor="middle">статистика</text>
      <rect x="136" y="3" width="76" height="23" fill="#E1E1E1" stroke="#ADADAD" stroke-width="1"/>
      <text x="174" y="18" text-anchor="middle">создание</text>
    </g>

    <rect x="12" y="143" width="396" height="364" fill="#FFFFFF" stroke="#ADADAD" stroke-width="1"/>
    <line x1="13" y1="143" x2="63" y2="143" stroke="#FFFFFF" stroke-width="2"/>

    <g transform="translate(24, 155)" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#000000">
      <rect x="0" y="0" width="44" height="25" fill="#FFFFFF" stroke="#ADADAD" stroke-width="1"/>
      <text x="22" y="17" text-anchor="middle">все</text>
      <rect x="44" y="2" width="94" height="23" fill="#E1E1E1" stroke="#ADADAD" stroke-width="1"/>
      <text x="91" y="17" text-anchor="middle">каждый день</text>
      <rect x="138" y="2" width="72" height="23" fill="#E1E1E1" stroke="#ADADAD" stroke-width="1"/>
      <text x="174" y="17" text-anchor="middle">на месяц</text>
      <rect x="210" y="2" width="102" height="23" fill="#E1E1E1" stroke="#ADADAD" stroke-width="1"/>
      <text x="261" y="17" text-anchor="middle">долгосрочные</text>
    </g>

    <rect x="24" y="179" width="372" height="316" fill="#F8F8F8" stroke="#D0D0D0" stroke-width="1"/>
    <line x1="25" y1="179" x2="67" y2="179" stroke="#F8F8F8" stroke-width="2"/>

    <text x="34" y="205" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#000000">сортировать:</text>
    <rect x="116" y="188" width="118" height="24" fill="#E1E1E1" stroke="#ADADAD" stroke-width="1"/>
    <text x="124" y="204" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#000000">по дедлайну</text>
    <path d="M 218 198 L 222 202 L 226 198" fill="none" stroke="#333333" stroke-width="1.2"/>

    <text x="386" y="205" text-anchor="end" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#000000">целей: 3</text>

    <rect x="34" y="220" width="352" height="232" fill="#FFFFFF" stroke="#828790" stroke-width="1"/>

    <g transform="translate(40, 228)">
      <rect x="0" y="0" width="13" height="13" fill="#FFFFFF" stroke="#333333" stroke-width="1"/>
      <path d="M 2.5 6.5 L 5.5 9.5 L 10.5 3.5" fill="none" stroke="#000000" stroke-width="1.5"/>
      <text x="20" y="11" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#000000">сдать курсовую | до 2026-11-26 | 9/10</text>
    </g>

    <g transform="translate(40, 250)">
      <rect x="0" y="0" width="13" height="13" fill="#FFFFFF" stroke="#333333" stroke-width="1"/>
      <path d="M 2.5 6.5 L 5.5 9.5 L 10.5 3.5" fill="none" stroke="#000000" stroke-width="1.5"/>
      <text x="20" y="11" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#000000">подготовить релиз | до 2026-11-26 | 8/10</text>
    </g>

    <g transform="translate(40, 272)">
      <rect x="0" y="0" width="13" height="13" fill="#FFFFFF" stroke="#333333" stroke-width="1"/>
      <text x="20" y="11" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#000000">нарядить елку | до 2026-12-06 | 10/10</text>
    </g>

    <rect x="34" y="460" width="76" height="25" fill="#E1E1E1" stroke="#ADADAD" stroke-width="1"/>
    <text x="72" y="477" text-anchor="middle" font-family="'Segoe UI', Arial, sans-serif" font-size="12" fill="#000000">удалить</text>

    <rect x="1" y="512" width="418" height="22" fill="#F0F0F0"/>
    <text x="10" y="527" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="#000000">целей: 3, выполнено: 2</text>
    <path d="M 412 532 L 417 527 M 408 532 L 417 523 M 404 532 L 417 519" stroke="#888888" stroke-width="1"/>
  </g>
</svg>






<!-- ABOUT THE PROJECT -->
## о проекте

Это мой первый проект в Яндекс Лицее. Он поможет вам систематизировать свои задачи и удобно распоряжаться дедлайнами своих целей.

Здесь можно:
* Создавать, изменять, отмечать цели
* Ставить дедлайны
* Смотреть статистику выполнений
* Сортировать задачи по разным критериям
* и т.д.

Разумеется, идея этого проекта не единственная в своем роде. Он прост в исполнении и использовании. Благодарю за внимание!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- BUILT WITH -->
## стек технологий

в этом разделе перечислены основные фреймворки, библиотеки и модули, использованные при создании проекта:

* Python3
* PyQt6
  * QtWidgets
  * QtCore
  * QtGui
* SQLite3
* CSV
* Datetime
* OS и Sys

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## начало работы

для локального запуска проекта выполните три простых шага:

1. **проверьте наличие python и pip** (версия python 3.8 или выше)
   ```sh
   python --version
   pip --version
   ```

2. **установите зависимости** из файла `requirements.txt` (фреймворк PyQt6)
   ```sh
   pip install -r requirements.txt
   ```

3. **запустите приложение**
   ```sh
   python main.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Создание целей
- [x] Сохранение отчета
- [ ] Добавить темную тему
- [ ] Добавить монетизацию
- [ ] Поддержка других языков
    - [ ] Французский
    - [ ] Немецкий


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Помоги проекту:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

GNU Affero General Public License v3.0 (AGPL). See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

<img width="400" height="400" alt="perekati-pole" src="https://github.com/user-attachments/assets/bb0dcef8-423e-47c5-8eea-38bef7894189" />
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <radialGradient id="shadowGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#5c4028" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#5c4028" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <ellipse cx="205" cy="342" rx="115" ry="18" fill="url(#shadowGrad)"/>
  <g stroke="#b89968" stroke-width="1.2" stroke-linecap="round" opacity="0.7">
    <path d="M 35 160 Q 75 150 110 165" fill="none"/>
    <path d="M 25 195 Q 65 188 95 202" fill="none"/>
    <path d="M 45 230 Q 80 225 105 235" fill="none"/>
    <circle cx="65" cy="142" r="2" fill="#b89968"/>
    <circle cx="40" cy="215" r="1.5" fill="#b89968"/>
    <circle cx="80" cy="250" r="2.2" fill="#b89968"/>
  </g>
  <g id="tumbleweed" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path d="M 182.4 178.9 C 125.9 95.5, 276.0 146.9, 244.7 167.7" stroke="#5e4126" stroke-width="2.16" opacity="0.9"/>
    <path d="M 246.0 208.7 C 290.6 288.3, 175.3 297.7, 178.1 230.3" stroke="#785534" stroke-width="2.46" opacity="0.9"/>
    <path d="M 209.4 176.1 C 286.9 157.3, 265.1 285.8, 226.9 294.1" stroke="#8f6942" stroke-width="1.57" opacity="0.9"/>
    <path d="M 290.1 262.7 C 269.3 297.5, 107.0 259.2, 99.6 238.7" stroke="#a67e51" stroke-width="2.39" opacity="0.9"/>
    <path d="M 241.6 123.7 C 279.0 156.3, 283.2 263.8, 205.6 286.8" stroke="#4a321b" stroke-width="1.54" opacity="0.9"/>
    <path d="M 203.8 234.9 C 178.7 307.6, 105.9 243.2, 107.8 203.1" stroke="#5e4126" stroke-width="3.09" opacity="0.9"/>
    <path d="M 148.6 131.1 C 167.2 94.7, 305.3 130.9, 274.5 132.3" stroke="#785534" stroke-width="2.4" opacity="0.9"/>
    <path d="M 156.4 99.8 C 250.2 106.1, 295.7 170.4, 249.8 224.7" stroke="#8f6942" stroke-width="3.1" opacity="0.9"/>
    <path d="M 240.3 160.4 C 300.9 144.7, 270.8 273.8, 207.0 270.3" stroke="#a67e51" stroke-width="2.41" opacity="0.9"/>
    <path d="M 193.3 283.2 C 78.7 283.7, 115.6 161.0, 170.7 135.4" stroke="#4a321b" stroke-width="1.48" opacity="0.9"/>
    <path d="M 267.7 255.8 C 198.5 310.4, 86.9 237.7, 127.0 198.9" stroke="#5e4126" stroke-width="3.15" opacity="0.9"/>
    <path d="M 216.8 179.9 C 298.2 167.4, 252.0 278.6, 208.9 295.9" stroke="#785534" stroke-width="2.18" opacity="0.9"/>
    <path d="M 84.7 234.5 C 109.9 160.9, 239.5 66.0, 239.6 156.6" stroke="#8f6942" stroke-width="1.94" opacity="0.9"/>
    <path d="M 144.8 134.2 C 124.3 89.2, 252.5 129.9, 270.4 124.0" stroke="#a67e51" stroke-width="1.98" opacity="0.9"/>
    <path d="M 317.0 214.4 C 253.6 273.5, 109.1 312.1, 99.4 244.1" stroke="#4a321b" stroke-width="1.55" opacity="0.9"/>
    <path d="M 168.2 202.8 C 114.6 121.5, 218.5 98.3, 271.5 124.5" stroke="#5e4126" stroke-width="2.97" opacity="0.9"/>
    <path d="M 159.1 221.4 C 94.7 186.5, 184.2 74.5, 200.9 99.3" stroke="#785534" stroke-width="2.19" opacity="0.9"/>
    <path d="M 163.1 195.9 C 101.5 176.2, 177.4 111.1, 206.5 134.9" stroke="#8f6942" stroke-width="2.54" opacity="0.9"/>
    <path d="M 215.2 314.5 C 116.6 296.6, 104.6 198.7, 173.4 168.3" stroke="#a67e51" stroke-width="3.08" opacity="0.9"/>
    <path d="M 134.8 168.8 C 171.4 111.2, 269.4 110.9, 304.6 174.4" stroke="#4a321b" stroke-width="2.24" opacity="0.9"/>
    <path d="M 187.9 108.5 C 270.7 118.5, 289.8 249.3, 221.0 238.5" stroke="#5e4126" stroke-width="1.74" opacity="0.9"/>
    <path d="M 136.3 221.3 C 93.0 239.5, 169.7 83.3, 185.9 144.3" stroke="#785534" stroke-width="1.49" opacity="0.9"/>
    <path d="M 308.6 199.5 C 282.5 251.9, 161.7 292.7, 90.8 245.6" stroke="#8f6942" stroke-width="2.12" opacity="0.9"/>
    <path d="M 258.7 222.7 C 263.4 295.7, 102.3 307.1, 141.1 199.8" stroke="#a67e51" stroke-width="3.19" opacity="0.9"/>
    <path d="M 109.0 166.8 C 80.0 176.6, 217.0 68.7, 213.9 139.9" stroke="#4a321b" stroke-width="1.5" opacity="0.9"/>
    <path d="M 135.0 162.0 C 145.2 125.8, 274.7 102.1, 249.1 197.6" stroke="#5e4126" stroke-width="2.62" opacity="0.9"/>
    <path d="M 203.4 236.8 C 133.5 305.5, 79.9 175.7, 167.3 153.2" stroke="#785534" stroke-width="2.34" opacity="0.9"/>
    <path d="M 241.7 181.9 C 324.6 228.5, 234.3 300.8, 179.8 252.8" stroke="#8f6942" stroke-width="2.75" opacity="0.9"/>
    <path d="M 263.6 231.2 C 206.0 300.1, 102.9 305.7, 76.1 186.1" stroke="#a67e51" stroke-width="2.99" opacity="0.9"/>
    <path d="M 245.0 157.4 C 290.5 114.9, 282.7 296.0, 284.6 270.4" stroke="#4a321b" stroke-width="1.41" opacity="0.9"/>
    <path d="M 222.5 149.9 C 287.0 163.3, 313.6 240.9, 252.9 307.2" stroke="#5e4126" stroke-width="1.89" opacity="0.9"/>
    <path d="M 123.5 140.8 C 133.3 104.1, 288.4 93.7, 253.0 124.7" stroke="#785534" stroke-width="1.57" opacity="0.9"/>
    <path d="M 153.3 224.3 C 112.5 254.8, 122.0 108.0, 121.9 130.7" stroke="#8f6942" stroke-width="2.17" opacity="0.9"/>
    <path d="M 232.5 202.0 C 301.6 292.8, 158.4 287.0, 96.2 252.5" stroke="#a67e51" stroke-width="1.63" opacity="0.9"/>
    <path d="M 158.9 307.3 C 130.8 272.3, 117.0 156.6, 166.6 92.6" stroke="#4a321b" stroke-width="2.8" opacity="0.9"/>
    <path d="M 249.0 156.3 C 323.0 134.5, 242.4 329.4, 205.2 248.6" stroke="#5e4126" stroke-width="2.99" opacity="0.9"/>
    <path d="M 297.5 215.3 C 335.3 233.1, 175.7 300.6, 163.0 312.9" stroke="#785534" stroke-width="2.82" opacity="0.9"/>
    <path d="M 287.3 270.5 C 244.3 306.3, 95.9 286.3, 145.3 193.9" stroke="#8f6942" stroke-width="1.81" opacity="0.9"/>
    <path d="M 243.8 206.6 C 303.4 213.6, 186.1 310.6, 166.3 307.6" stroke="#a67e51" stroke-width="3.17" opacity="0.9"/>
    <path d="M 84.1 173.2 C 73.4 128.8, 182.1 107.7, 205.1 77.8" stroke="#4a321b" stroke-width="2.18" opacity="0.9"/>
    <path d="M 192.4 144.1 C 249.7 88.5, 328.2 178.3, 272.4 236.3" stroke="#5e4126" stroke-width="1.4" opacity="0.9"/>
    <path d="M 270.4 164.5 C 309.4 200.6, 263.4 310.5, 168.7 296.8" stroke="#785534" stroke-width="1.99" opacity="0.9"/>
    <path d="M 155.8 304.1 Q 154.1 317.1 154.6 332.4" stroke="#5e4126" stroke-width="1.3"/>
    <path d="M 267.6 269.6 Q 282.0 290.7 293.5 316.7" stroke="#785534" stroke-width="1.55"/>
    <path d="M 292.0 200.2 Q 313.1 203.4 335.0 207.9" stroke="#8f6942" stroke-width="1.21"/>
    <path d="M 86.6 219.3 Q 75.7 233.3 64.4 244.2" stroke="#a67e51" stroke-width="1.34"/>
    <path d="M 245.6 100.5 Q 239.7 81.1 245.2 67.9" stroke="#4a321b" stroke-width="1.48"/>
    <path d="M 249.3 132.0 Q 269.0 107.3 284.0 82.8" stroke="#5e4126" stroke-width="1.24"/>
    <path d="M 154.7 132.3 Q 143.1 110.0 133.4 95.4" stroke="#785534" stroke-width="1.96"/>
    <path d="M 117.4 190.6 Q 98.2 190.9 71.9 187.2" stroke="#8f6942" stroke-width="1.99"/>
    <path d="M 103.5 134.0 Q 94.4 126.1 85.2 110.2" stroke="#a67e51" stroke-width="1.55"/>
    <path d="M 287.2 134.3 Q 295.7 124.7 301.0 108.7" stroke="#4a321b" stroke-width="1.52"/>
    <path d="M 136.0 134.6 Q 117.4 125.6 103.1 115.6" stroke="#5e4126" stroke-width="1.14"/>
    <path d="M 212.6 306.5 Q 225.8 321.4 237.9 338.3" stroke="#785534" stroke-width="1.21"/>
    <path d="M 99.0 255.4 Q 90.1 251.4 74.9 250.2" stroke="#8f6942" stroke-width="1.01"/>
    <path d="M 134.7 287.9 Q 119.1 302.9 97.6 316.7" stroke="#a67e51" stroke-width="1.6"/>
    <path d="M 216.5 287.9 Q 233.8 308.4 246.9 331.1" stroke="#4a321b" stroke-width="1.17"/>
    <path d="M 115.8 217.5 Q 94.3 219.7 71.2 233.3" stroke="#5e4126" stroke-width="1.64"/>
    <path d="M 264.9 274.2 Q 274.7 283.9 288.6 287.4" stroke="#785534" stroke-width="1.38"/>
    <path d="M 201.4 87.6 Q 192.1 84.7 181.9 69.8" stroke="#8f6942" stroke-width="1.35"/>
    <path d="M 135.1 110.5 Q 128.5 87.4 129.1 75.9" stroke="#a67e51" stroke-width="1.15"/>
    <path d="M 274.6 275.8 Q 293.4 286.2 305.8 304.5" stroke="#4a321b" stroke-width="1.61"/>
    <path d="M 198.9 114.5 Q 204.6 84.9 221.8 59.8" stroke="#5e4126" stroke-width="1.68"/>
    <path d="M 292.8 175.0 Q 312.0 169.2 328.1 173.0" stroke="#785534" stroke-width="1.77"/>
    <path d="M 261.1 116.2 Q 275.4 109.0 293.4 103.6" stroke="#8f6942" stroke-width="1.37"/>
    <path d="M 106.0 196.5 Q 88.2 207.3 59.3 214.9" stroke="#a67e51" stroke-width="1.83"/>
    <path d="M 174.1 105.9 Q 183.7 87.5 185.9 68.2" stroke="#4a321b" stroke-width="1.48"/>
    <path d="M 100.1 242.8 Q 81.5 244.6 72.9 237.3" stroke="#5e4126" stroke-width="1.24"/>
    <path d="M 98.4 222.9 Q 83.4 214.4 76.0 212.8" stroke="#785534" stroke-width="1.8"/>
    <path d="M 138.6 296.3 Q 142.0 307.8 134.6 329.2" stroke="#8f6942" stroke-width="1.72"/>
  </g>
</svg>

(не связывайтесь со мной)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
