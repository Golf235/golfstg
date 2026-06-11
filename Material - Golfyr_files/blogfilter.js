$( document ).ready(function() {
	
	let currentPage = 1;
	
	$('.cat-list_item').on('click', function(e) {
		e.preventDefault();
		$('.cat-list_item').removeClass('active');
		$(this).addClass('active');
		
		let currentCatSlug = $(this).data('slug');
		
		// Construct URLSearchParams object instance from current URL querystring.
		//var queryParams = new URLSearchParams(window.location.search);
		//let currentUrl = new URL(window.location.href);
		//currentUrl.searchParams.set('cat', currentUrl);
		//window.location.href = currentUrl;

		// Set new or modify existing parameter value. 
		//queryParams.set("cat", currentCatSlug );

		// Replace current querystring with the new one.
		//history.pushState(null, null, "?"+queryParams.toString());

		$.ajax({
			type: 'POST',
			url: wpAjax.ajaxUrl,
			dataType: 'html',
			data: {
				action: 'blog_get_sticky',
				category: $(this).data('slug'),
				//category: 'blog',
				show: 'sticky',
			},
			success: function(result) {
				$('.sticky-tiles').html(result);
				//$('.sticky-tiles').html(result.html);
				//$('.sticky-tiles').append(result.html);
			},
			error: function(xhr, status, error) {
				console.log(error);
			}
		});
				
		//let currentPage = 1;
			
		$.ajax({
			type: 'POST',
			url: wpAjax.ajaxUrl,
			dataType: 'json',
			data: {
				action: 'blog_get_all_posts',
				category: $(this).data('slug'),
				paged: currentPage,
			},
			success: function(result) {
				//$('.blog-tiles').html(result);
				$('.blog-tiles').html(result.html);
				//$('.blog-tiles').append(result.html);
				$('.load-more-btn').attr('data-slug', currentCatSlug);
				//console.log('All Posts per CAT Page: ' + currentPage);
				//console.log('RESULT MAX: ' + result.max + ' Current Cat: ' + currentCatSlug);
				if(result.max > 1) { 
					//$('#load-more').show();
					$('#load-more').removeClass('hide');
					$('#load-more').addClass('show');
					//console.log('Show Load More');
				} else {
					$('#load-more').removeClass('show');
					$('#load-more').addClass('hide');
					//console.log('Hide Load More');
				}
				currentPage = 1;
			},
			error: function(xhr, status, error) {
				console.log(error);
			}
		});
    });
	
	
	$('#load-more').on('click', function(e) {
	    currentPage++; // Do currentPage + 1, because we want to load the next page
	    //console.log('Load more pressed... ' + currentPage);
        $.ajax({
            type: 'POST',
            url: wpAjax.ajaxUrl,
            dataType: 'json',
            data: {
                action: 'blog_get_all_posts',
                category: $(this).data('slug'),
                paged: currentPage,
            },
            success: function (result) {
                if(currentPage >= result.max) {
                    //$('#load-more').hide();
                    $('#load-more').removeClass('show');
					$('#load-more').addClass('hide');
                    //console.log('Load next Page: ' + currentPage + ' Result Max: ' + result.max);
                    currentPage = 1;
                    //console.log('Back to Page: ' + currentPage + ' Result Max: ' + result.max);
                }
               $('.blog-tiles').append(result.html);
            }
        });
	})
});