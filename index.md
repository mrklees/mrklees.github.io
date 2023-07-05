---
layout: single
hidden: true
header:
  overlay_color: "#5e616c"
  overlay_image: https://static.cloudygo.com/static/Critical Theme Camp - Inspiration/Kaylie art brunch.jpg
excerpt: Exploring beauty through art and sound

feature_row:
  - title: "DeComposers"
    alt: "DeComposers @ Solstice Parade"
    url: "/events/fremont-solstice-parade"
    image_path: "https://static.cloudygo.com/static/2023-SolsticeParade/Decomposers_at_Parade.jpg"
    excerpt: "DeComposters at the Fremont Solstice Parade"
    btn_label: "DeComposters @ Solstice Parade"
    btn_class: "btn--info"

  - title: "ReIgnition"
    alt: "The River @ ReIgnition 2023"
    url: "/events/reignition"
    image_path: "https://static.cloudygo.com/static/2023-ReIgnition/RiverHeader.jpg"
    excerpt: Haus Anima presents The River!
    btn_label: "The River @ ReIgnition"
    btn_class: "btn--info"

  - title: "Petit Troll"
    alt: "2023 Petit Troll Parade and Mardi Gras celebration"
    url: "/events/petit-troll-parade"
    image_path: "https://static.cloudygo.com/static/2023-PetitTroll/powerhouse-floats_thumb.jpg"
    excerpt: |
      Petit Mardi Gras Parade Floats!
    btn_label: "Petit Troll Parade"
    btn_class: "btn--info"

  - title: "Flutterfish"
    alt: "Flutterfish"
    url: "/events/flutterfish"
    image_path: "https://static.cloudygo.com/static/Flutterfish/3FlutterHung_thumb.jpg"
    excerpt: |
      Flutterfish at Wintertide Festival of Lights
    btn_label: "Flutterfish in the Forest"
    btn_class: "btn--info"

  - title: "Seacompression!"
    alt: "Mourning Owl at World's End Faire"
    url: "/events/seacompression"
    image_path: "https://static.cloudygo.com/static/Seacompression 2022/100 Worlds End Faire_thumbnail.jpg"
    excerpt: |
      Haus Anima unveils our Mourning Owl experience!
    btn_label: "See our Seacompression experience!"
    btn_class: "btn--info"

  - title: "Fall Equinox at Luminata!"
    alt: "BettaFish Sculpture"
    url: "/events/luminata"
    image_path: "https://static.cloudygo.com/static/BettaFish/BettaFish_thumbnail.jpg"
    excerpt: |
      Interactive Illuminated Betta Fish Sculpture!
    btn_label: "See our Interactive Betta Fish Sculpture!"
    btn_class: "btn--info"

  - title: "Critical 2022!"
    alt: "Critical 2022 Poster"
    url: "/events/critical-wrap"
    image_path: "https://static.cloudygo.com/static/Critical%202022/CriticalPoster_thumb.jpg"
    excerpt: |
      Friends! Art! Collaboration! Electroluminescent menagerie!
    btn_label: "Read our Critical Summary"
    btn_class: "btn--info"


  - title: "Remergence 2022"
    alt: "Haus Anima's first public event!"
    url: "/events/remergence-wrap"
    image_path: "https://static.cloudygo.com/static/ReIgnition%202022%20Remergence/IMG_1381_thumb.jpg"
    excerpt: |
      Space! Collaborative art! Music!
    btn_label: "Read our Remergence Summary"
    btn_class: "btn--info"

  - title: "Lily Pad Temple under Moon's Light"
    alt: Pixel art and 8-bit adventure!
    url: "art/lily-pad-temple/"
    image_path: "https://static.cloudygo.com/static/LilyPad/lilypadtemple2.png"
    excerpt: Pixel art and 8-bit adventure!
    btn_label: "Pixel Art and 8-bit sounds!"
    btn_class: "btn--info"

---

<h2 class="archive__subtitle">Upcoming events!</h2>
<div>
  <p>
    You can join Haus Anima at
    <a href="https://fremontartscouncil.org/may-day">The FAC's Solstice May Day</a> (April 30th)
    and later at FAC's Solstice Parade!
  </p>
  <p>
    Over the next few months we'll be busy creating Dream Willow and Hades to pair with
    <a href="/events/reignition">The River</a> for Critical 2023.
  </p>
</div>


{::comment}
<h2 class="archive__subtitle">Recent Art and Events</h2>
<div markdown="block">
 * **The River** at [ReIgnition](/events/reignition)
 * **Mourning Owl** at [Seacompression](/events/seacompression)
 * **Interactive Illuminated Betta Fish Sculpture** at [Luminata](/events/luminata)
</div>
{:/}

<h3 class="archive__subtitle">Haus Anima Write-ups</h3>
<div class="index-feature-row">
  {% include feature_row %}
</div>


<h3 class="archive__subtitle">{{ site.data.ui-text[site.locale].recent_posts | default: "Recent Posts" }}</h3>

{% if paginator %}
  {% assign posts = paginator.posts %}
{% else %}
  {% assign posts = site.posts %}
{% endif %}

{% assign entries_layout = page.entries_layout | default: 'list' %}
<div class="entries-{{ entries_layout }}">
  {% for post in posts %}
    {% include archive-single.html type="entries_layout" %}
  {% endfor %}
</div>

{% include paginator.html %}
