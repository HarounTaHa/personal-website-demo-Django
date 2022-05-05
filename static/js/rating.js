document.addEventListener("DOMContentLoaded",function(){
  document.querySelectorAll(".rating").forEach(function(el) {
    ratingHoverStars(el);
  });
});

// the mouseover hover effect
// the mouseout reset to data-default
// the click event to save the star rating & update data-default

function ratingHoverStars( el ) {
  console.log("ratingHoverStars", el)
  el.querySelectorAll("div").forEach( function(div,index) {
    // attach the mousover effect for star hovering
    div.addEventListener("mouseover",(function(){
      let starNum = index+1;
      return function(event){
        setStarRating(el,starNum);
      };
    })());
    // attach the mouseout event for resetting
    el.addEventListener("mouseout",function(event){
      setDefaultRating(el);
    });
    // and also reset
    setDefaultRating(el);
  });
}
function setDefaultRating(el){
  setStarRating(el,~~el.getAttribute("data-default"));
}

/* Set the Star Rating
 *
 * @param elRating - the rating element container w/ stars inside
 * @param stars - the number of stars to active (0-5)
 */
function setStarRating( elRating, stars ) {
  elRating.querySelectorAll("div").forEach(function(div,index){
    if( index+1 <= stars ) {
      div.classList.add("active");
    } else {
      div.classList.remove("active");
    }
  });
}
