---
layout: page
title: Book Library
permalink: /books/
---

<link rel="stylesheet" href="/assets/css/book-library.css">

<div class="book-library-header">
  <h1> My Library</h1>
  <p>Books organized by genre that I've read and currently reading. I lost my old goodreads account, so just adding books on the list based on my recent reads.</p>
  <a href="https://www.goodreads.com/review/list/73241023?shelf=%23ALL%23" target="_blank" class="goodreads-link-simple">
    View full library on Goodreads →
  </a>
</div>

<!-- Currently Reading -->
<div class="book-shelf">
  <h2>📖 Currently Reading</h2>
  <div class="book-slider-container">
    <button class="slider-arrow left" onclick="scrollSlider(this, -300)">
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
      </svg>
    </button>
    <div class="book-grid">
      
      <!-- Template: Duplicate for each book -->
      <div class="book-item">
        <div class="book-cover">
          <img src="/assets/books/anxious-people.jpg" alt="Anxious People">
        </div>
        <div class="book-title">Anxious People</div>
        <div class="book-author">Fredrik Backman</div>
      </div>

      <div class="book-item">
        <div class="book-cover">
          <img src="/assets/books/body-keeps-score.jpg" alt="The Body Keeps the Score">
        </div>
        <div class="book-title">The Body Keeps the Score</div>
        <div class="book-author">Bessel van der Kolk</div>
      </div>

      <div class="book-item">
        <div class="book-cover">
          <img src="/assets/books/the-testaments.jpg" alt="The Testamentse">
        </div>
        <div class="book-title">The Testaments</div>
        <div class="book-author">Margaret Atwood</div>
      </div>
      
    </div>
    <button class="slider-arrow right" onclick="scrollSlider(this, 300)">
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
      </svg>
    </button>
  </div>
</div>


<!--  Science Fiction & Fantasy -->
<!-- <div class="book-shelf">
  <h2>🚀 Science Fiction & Fantasy</h2>
  <div class="book-slider-container">
    <button class="slider-arrow left" onclick="scrollSlider(this, -300)">
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
      </svg>
    </button>
    <div class="book-grid">
      
      <div class="book-item">
        <div class="book-cover">
          <div class="book-cover-placeholder">
            <span>📗</span>
            <p>Book Cover</p>
          </div>
        </div>
        <div class="book-title">Book Title</div>
        <div class="book-author">Author Name</div>
      </div>
      
    </div>
    <button class="slider-arrow right" onclick="scrollSlider(this, 300)">
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
      </svg>
    </button>
  </div>
</div>

<!-- Technology & Computer Science -->
<!-- <div class="book-shelf">
  <h2>💻 Technology & Computer Science</h2>
  <div class="book-slider-container">
    <button class="slider-arrow left" onclick="scrollSlider(this, -300)">
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
      </svg>
    </button>
    <div class="book-grid">
      
      <div class="book-item">
        <div class="book-cover">
          <div class="book-cover-placeholder">
            <span>📘</span>
            <p>Book Cover</p>
          </div>
        </div>
        <div class="book-title">Book Title</div>
        <div class="book-author">Author Name</div>
      </div>
      
    </div>
    <button class="slider-arrow right" onclick="scrollSlider(this, 300)">
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
      </svg>
    </button>
  </div>
</div> -->

<!-- Psychology & Human Behavior -->
<!-- <div class="book-shelf">
  <h2>🧠 Psychology & Human Behavior</h2>
  <div class="book-slider-container">
    <button class="slider-arrow left" onclick="scrollSlider(this, -300)">
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
      </svg>
    </button>
    <div class="book-grid">
      
      <div class="book-item">
        <div class="book-cover">
          <div class="book-cover-placeholder">
            <span>📙</span>
            <p>Book Cover</p>
          </div>
        </div>
        <div class="book-title">Book Title</div>
        <div class="book-author">Author Name</div>
      </div>
      
    </div>
    <button class="slider-arrow right" onclick="scrollSlider(this, 300)">
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
      </svg>
    </button>
  </div>
</div>

<!-- Philosophy & Ethics -->
<!-- <div class="book-shelf">
  <h2>🤔 Philosophy & Ethics</h2>
  <div class="book-slider-container">
    <button class="slider-arrow left" onclick="scrollSlider(this, -300)">
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
      </svg>
    </button>
    <div class="book-grid">
      
      <div class="book-item">
        <div class="book-cover">
          <div class="book-cover-placeholder">
            <span>📔</span>
            <p>Book Cover</p>
          </div>
        </div>
        <div class="book-title">Book Title</div>
        <div class="book-author">Author Name</div>
      </div>
      
    </div>
    <button class="slider-arrow right" onclick="scrollSlider(this, 300)">
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
      </svg>
    </button>
  </div> 
</div>-->

<!-- Education & Teaching -->
<!-- <div class="book-shelf">
  <h2>🎓 Education & Teaching</h2>
  <div class="book-slider-container">
    <button class="slider-arrow left" onclick="scrollSlider(this, -300)">
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
      </svg>
    </button>
    <div class="book-grid">
      
      <div class="book-item">
        <div class="book-cover">
          <div class="book-cover-placeholder">
            <span>📓</span>
            <p>Book Cover</p>
          </div>
        </div>
        <div class="book-title">Book Title</div>
        <div class="book-author">Author Name</div>
      </div>
      
    </div>
    <button class="slider-arrow right" onclick="scrollSlider(this, 300)">
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
      </svg>
    </button>
  </div>
</div>  -->

<!-- Non-Fiction & Biography -->
<!-- <div class="book-shelf">
  <h2>📖 Non-Fiction & Biography</h2>
  <div class="book-slider-container">
    <button class="slider-arrow left" onclick="scrollSlider(this, -300)">
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
      </svg>
    </button>
    <div class="book-grid">
      
      <div class="book-item">
        <div class="book-cover">
          <div class="book-cover-placeholder">
            <span>📒</span>
            <p>Book Cover</p>
          </div>
        </div>
        <div class="book-title">Book Title</div>
        <div class="book-author">Author Name</div>
      </div>
      
    </div>
    <button class="slider-arrow right" onclick="scrollSlider(this, 300)">
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
      </svg>
    </button>
  </div>
</div> -->

<!-- Fiction & Literature -->
<!-- <div class="book-shelf">
  <h2>📚 Fiction & Literature</h2>
  <div class="book-slider-container">
    <button class="slider-arrow left" onclick="scrollSlider(this, -300)">
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
      </svg>
    </button>
    <div class="book-grid">
      
      <div class="book-item">
        <div class="book-cover">
          <div class="book-cover-placeholder">
            <span>📕</span>
            <p>Book Cover</p>
          </div>
        </div>
        <div class="book-title">Book Title</div>
        <div class="book-author">Author Name</div>
      </div>
      
    </div>
    <button class="slider-arrow right" onclick="scrollSlider(this, 300)">
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
      </svg>
    </button>
  </div>
</div>   -->

<script>
function scrollSlider(button, amount) {
  const container = button.parentElement;
  const slider = container.querySelector('.book-grid');
  slider.scrollBy({ left: amount, behavior: 'smooth' });
}
</script>
