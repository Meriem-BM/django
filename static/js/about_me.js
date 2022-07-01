/*
OVERVIEW
A simple vertical carousel

Slides are cycled through by the two toggles on the right, previous and next. 

Next
=> toggle clicked
=> active slide is faded out, moved up
=> next slide is faded in, moved up

Previous
=> toggle clicked
=> active slide is faded out, moved down
=> next slide is faded in, moved down
*/

$(document).ready(function() {
  
    // slide to start. should always be 1 as it's also the lower bound to the number of slides. corresponds to [pos] attribute on html element
    let active_slide = 1;
    
    // last slide. should be the upper bound to the number of slides. corresponds to [pos] attribute on html element
    let slide_count = 3;
    
    // speed of animations (ms)
    let speed = 400;
    
    document.getElementsByClassName("swiper-pagination-bullet")[0].classList.add('swiper-pagination-bullet-active');
    document.getElementsByClassName("slide-toggle")[0].style.color = "#70A288";

    // hide all slides that aren't starting active slide
    $(".slide[pos!='" + active_slide + "']").each(function() {
      $(this).hide();
    })

    // The list of sliders, by selectiing the element with className='slide-toggle'
    let list = document.getElementsByClassName('slide-toggle');

    // Show the slider that it's clicked from the 3 sliders
    for (let i = 1; i <= list.length; i++) {

    $(".slide-toggle[direction='" + i + "']").click(function() {
        
        var direction;
        (document.direction !=undefined)? direction = document.direction : direction =document.getElementsByClassName("slide-toggle")[i-1].getAttribute("direction");
        
        let clicked_slide = parseInt(direction);
        
        if (clicked_slide > active_slide) {
            Next(active_slide, clicked_slide, slide_count, speed);
        }      
        else if (clicked_slide < active_slide) {
            Prev(active_slide, clicked_slide, slide_count, speed);
        }
        // once animations are done, set new active slide
            active_slide = clicked_slide;

            document.getElementsByClassName("swiper-pagination-bullet")[(clicked_slide-1)].classList.add('swiper-pagination-bullet-active');
            document.getElementsByClassName("slide-toggle")[(clicked_slide-1)].style.color = "#70A288";

            for (let i = 0; i < list.length; i++) {
                if (i!=clicked_slide-1){
                    document.getElementsByClassName("swiper-pagination-bullet")[i].classList.remove('swiper-pagination-bullet-active');
                    document.getElementsByClassName("slide-toggle")[i].style.color = "white";
                }
            }
    })

    }
    
    
  })
  
  
  function Next(active_slide, next_slide, slide_count, speed) {
    
  // non active slides moved down so they can slide up when activated
    $(".slide[pos!='" + active_slide + "']").each(function() {
        $(this).css("top", "10px");
      })
    
      
      if (next_slide <= slide_count) {
        
        
        /*   
        Note: delay only works if .hide() or .show() are in its internal queue. Therefore you need to pass an argument to it, even if it's 0. (praise be to stackoverflow)
        */
        
        $(".slide[pos='" + active_slide + "']").animate({opacity:0, top: "-10px"}, {duration: speed}).hide(0).animate({top: "10px"});
        
        $(".slide[pos='" + next_slide + "']").delay(speed).show(0).animate({opacity:1, top: "0px"}, {duration: speed});  
        
      } else {
        
        next_slide = 1;
          
        $(".slide[pos='" + active_slide + "']").animate({opacity:0, top: "-10px"}, {duration: speed}).hide(0).animate({top: "10px"});
        
        $(".slide[pos='" + next_slide + "']").delay(speed).show(0).animate({opacity: 1, top: "0px"});
                
      }
      
  }
  
  function Prev(active_slide, next_slide, slide_count, speed) {
    
    // non active slides moved up so they can slide down when activated
      $(".slide[pos!='" + active_slide + "']").each(function() {
        $(this).css("top", "-10px");
      })
      
      
      if (next_slide < 1) {
  
        next_slide = slide_count;
        
        $(".slide[pos='" + active_slide + "']").animate({opacity:0, top: "10px"}, {duration: speed}).hide(0).animate({top: "10px"});
        
        $(".slide[pos='" + next_slide + "']").delay(speed).show(0).animate({opacity:1, top: "0px"}, {duration: speed});
                
        
      } else {
       
        
        $(".slide[pos='" + active_slide + "']").animate({opacity:0, top: "10px"}, {duration: speed}).hide(0).animate({top: "10px"});
        
        $(".slide[pos='" + next_slide + "']").delay(speed).show(0).animate({opacity: 1, top: "0px"});        
        
      }
    
  }
