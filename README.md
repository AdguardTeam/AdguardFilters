#Experimental filter for Adguard

Filter designed to test certain hazardous filtering rules before they are added to the main filters.
Subsequently filter rules that pass verification will be added to one of our main filter.

All changes contributed to the Experimental filter will be available for users in the course of 1 hour from the moment they were added.

Discussions are held on Adguard’s official forum: 
http://forum.adguard.com/showthread.php?578-Adguard-Experimental-Filter

##How to join

If you want to join Experimental filter development you can request it in experimental filter topic.
Becoming a committer here is not simple. Each request is reviewed by us considering your activity.

##How to develop filters

There is an article on our web site about filter rules syntax:
http://adguard.com/filterrules.html

Reading this article is mandatory for proper filters creation.

Adguard's filter rules syntax extends Adblock plus syntax.
URL blocking rules and Element hiding rules are pretty the same.
So here is a good article from ABP web site explaining these types of rules:
https://adblockplus.org/en/filter-cheatsheet

##Work rules

1. Don’t use any language other than English if you are editing file using web interface.
2. All new rules must be checked in User Filter before adding to the file. 
3. Experimental filter is divided in a number of sections

*English* - rules for English filter
*Social* - rules for Social Media filter
*Spyware* - rules for Spyware filter
*Russian* - rules for Russian filter
*Other* - rules for other filters

4. Each section could be divided in a number of smaller sections.

*advertising_networks.txt*

Advertising networks known rotator domains. This section contains the list of rules blocking requests to known rotator domains of the advertising networks.
For example, "*.doubleclick.net" are rotator domains of Doubleclick ad network.

*direct_adverts.txt*

Contains rules which are blocking URLs to direct adverts. What do we mean by direct adverts - it is all kind of advertisers who are not ad networks. For example, rules that block referral links.

*common_urls_unsorted.txt*

URL blocking rules unsorted list.
You can read more about URL blocking rules here:
http://adguard.com/filterrules.html#baseRules

Add basic rule here if it cannot be added to direct_adverts.txt or advertising_networks.txt.
For example rules like `http://example.com/banner.png` blocking specific URL should be added to this section.

*common_css.txt*

Common CSS rules. Learn more here: http://adguard.com/filterrules.html#hideRules
This section contains CSS rules without domain restrictions. Be cautious and add rules here even if you are sure that this rule could be used for more than one web site.

*common_html.txt*

Common HTML rules. Learn more about HTML rules here: http://adguard.com/filterrules.html#htmlContentFilter.

This section contains the list of common HTML rules without domain restrictions.
*Be aware that rules added to this section cannot be used by Adguard extensions.*
We advise you to stick to CSS/Javascript/URL rule types and use HTML rules if there is no other way only.

*common_js.txt*

Common javascript rules. Learn more about javascript rules here: http://adguard.com/filterrules.html#javascriptInjection.
Javascript rules which are not restricted to specific domains. Be VERY cautious with this type of rules.

*specific_web_sites.txt*

Rules that are restricted to one or more domains. This section contain any type of rule grouped by domain.

*whitelist.txt*

This section contains all kinds of exception rules.

Learn more about exceptions:
http://adguard.com/filterrules.html#exclusionRules
http://adguard.com/filterrules.html#hideRulesExceptions
http://adguard.com/filterrules.html#cssInjectionExceptions
http://adguard.com/filterrules.html#javascriptInjectionExceptions












#Project description in Russian
Все изменения, внесенные в стандартный фильтр, будут доступны в программе в течении 1 часа с момента внесения.

Обсуждения ведутся на форуме Adguard: 
http://forum.adguard.ru/showthread.php?t=458.

##Как присоединиться к проекту
Если вы хотите присоединиться к разработчикам экспериментального фильтра,
подайте заявку на форуме в теме-обсуждении экспериментального фильтра.
Мы принимаем не всех, каждая заявка рассматривается индивидуально с учетом вашей деятельности.

##Как разрабатывать фильтры
Любому, кто хочет научиться разрабатывать фильтры, необходимо ознакомиться со статьей,
описывающей правила создания фильтров Adguard:
http://adguard.com/filterrules.html

Синтаксис правил фильтрации Adguard расширяет синтаксис правил Adblock Plus.
Проще говоря, правила блокировки по URL и правила сокрытия работают практически одинаково.

Так что вам может очень пригодиться статья с сайта ABP, описывающая в деталях составление
правил этих типов:
https://adblockplus.org/en/filter-cheatsheet

##Основные правила работы:

1. Если для редактирования используется веб-интерфейс, пишем либо на английском, либо транслитом (русские буквы превращаются в тыкву).
2. Перед добавлением правило обязательно нужно проверить в пользовательском фильтре.
3. Экспериментальный фильтр разбит на несколько секций

*English* - правила для английского фильтра
*Social* - правила для фильтра виджетов соцсетей
*Spyware* - правила для фильтра счетчиков
*Russian* - правила для русского фильтра
*Other* - правила для остальных фильтров

4. Каждая секция может быть разбита на меньшие секции

*advertising_networks.txt*

Содержит известные откруточные домены рекламных сетей. Этот фильтр содержит только правила блокировки по URL, блокирующие, обычно, домены, с которых загружаются скрипты рекламных сетей. К примеру, "*.doubleclick.net" это откруточные домены рекламной сети Doubleclick.

*direct_adverts.txt*

Содержит правила блокировки по URL прямых рекламодателей.
Под прямыми рекламодателями мы понимаем тех, кто не использует услуги рекламных сетей, а для показа рекламы использует промо-материалы, которые располагаются прямо на их собственных сайтах. Под этот фильтр подходят разные правила, например правила, блокирующие реферальные ссылки, или правила, блокирующие third-party картинки с сайта рекламодателя.

*common_urls_unsorted.txt*

Общий список правил блокировки по URL.
Подробнее о таких правилах: http://adguard.com/filterrules.html#baseRules

Сюда правила добавляются в том случае, если они не подходят ни под одну другую секцию (direct_adverts, adveritising_networks, specific_web_sites);
К примеру, правило вида `http://example.com/banner.png`, блокирующее конкретную картинку, может быть добавлено в эту секцию.

*common_css.txt*

Общие CSS правила (правила сокрытия элементов, правила вставки CSS). Эта секция содержит CSS правила без ограничения на конкретные домены.
Будьте осторожны при добавлении правил в эту секцию. Удостоверьтесь, что эти правила будут использоваться больше, чем на одном сайте.

*common_html.txt*

Секция содержит общие HTML правила без ограничения на конкретные сайты.
*Обратите внимание, что правила этого типа не работают в браузерных расширениях Adguard*.
Мы не рекомендуем добавлять правила этого типа. Только если другого пути уже нет.

*common_js.txt*

Общие Javascript-правила, не ограниченные конкретным доменом.
Будьте ОЧЕНЬ осторожны с этим типом правил.

*specific_web_sites.txt*

Правила, действие которых ограничено одним или более конкретными доменами.
Правила в этой секции должны быть сгруппированы по доменам-ограничениям.

*whitelist.txt*

*Все правила-исключения должны предворяться комментарием, описывающим зачем нужно это правило (или, например, ссылкой на обсуждение проблемы на форуме).*

Секция содержит все виды правил-исключений:
http://adguard.com/filterrules.html#exclusionRules
http://adguard.com/filterrules.html#hideRulesExceptions
http://adguard.com/filterrules.html#cssInjectionExceptions
http://adguard.com/filterrules.html#javascriptInjectionExceptions
