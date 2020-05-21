document.addEventListener('DOMContentLoaded', () => {

    // Just check if the page is loaded from a back button then reload it with original data
    // otherwise what will happen is that our data will update later in the page and hence 
    // script wont update the cost.
    if(performance.navigation.type == 2){
        location.reload(true);
     }

    // Get initial price of item as this is what we set by default in the page.
    const individual_item_price = parseFloat(document.getElementById('individual-item-price').innerHTML);
    var cur_quantity = 1;
    var individual_extra_cost = 0 ;

    function fnUpdateTotalCost()
    {
        if (cur_quantity < 1 )
            cur_quantity = 1 ;
        if (individual_extra_cost < 0 )
        individual_extra_cost = 0 ;
        let totalcost = ( ( individual_item_price + individual_extra_cost ) * cur_quantity ).toFixed(2) ;
        document.getElementsByName('total-price')[0].value = totalcost ;
    } ;

    // When quantity changed,
    document.querySelector('#quantity').onchange = function() {
        cur_quantity = this.value;
        fnUpdateTotalCost() ;
    };
    

    function fnUpdateForExtraCost ()
    {
        let extra_id = parseInt ( this.value ) ;
        let extra_element_node_name = `extra_price-${extra_id}` ;
        let extra_price_node = document.getElementById (extra_element_node_name) ;
        let extra_price = 0 ;
        if ( extra_price_node )
            extra_price = parseFloat ( extra_price_node.innerText ) ;
        if (this.checked) {
            individual_extra_cost += extra_price;
        } else {
            individual_extra_cost -= extra_price;
        };
        fnUpdateTotalCost() ;
    }

    // If extra exists,
    {
        let extraNodes = document.getElementsByClassName('extrasub') ;
        for ( let i = 0 ; i < extraNodes.length ; i++)
        {
            extraNodes[i].addEventListener ( 'change' , fnUpdateForExtraCost , false ) ;
        }
    }
});

