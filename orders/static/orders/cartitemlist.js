function fnCheckOut()
{
    // let finalprice = document.getElementById("cart-total-cost").innerText ;
    // confirmationstring = `Are yo sure you want to place a order of final value ${finalprice}?`;
    // let answer = confirm(confirmationstring)
    // if (false == answer)
    //     return false;

    custdetailformbutton = document.getElementById("Customer-details-form-submit");
    custdetailformbutton.click();
}

document.addEventListener('DOMContentLoaded', () => {

  
    
    // function fnUpdateTotalCost()
    // {
    //     if (cur_quantity < 1 )
    //         cur_quantity = 1 ;
    //     if (individual_extra_cost < 0 )
    //     individual_extra_cost = 0 ;
    //     let totalcost = ( ( individual_item_price + individual_extra_cost ) * cur_quantity ).toFixed(2) ;
    //     document.getElementsByName('total-price')[0].value = totalcost ;
    // } ;

    // // When quantity changed,
    // document.querySelector('#quantity').onchange = function() {
    //     cur_quantity = this.value;
    //     fnUpdateTotalCost() ;
    // };
    

    // function fnUpdateForExtraCost ()
    // {
    //     let extra_id = parseInt ( this.value ) ;
    //     let extra_element_node_name = `extra_price-${extra_id}` ;
    //     let extra_price_node = document.getElementById (extra_element_node_name) ;
    //     let extra_price = 0 ;
    //     if ( extra_price_node )
    //         extra_price = parseFloat ( extra_price_node.innerText ) ;
    //     if (this.checked) {
    //         individual_extra_cost += extra_price;
    //     } else {
    //         individual_extra_cost -= extra_price;
    //     };
    //     fnUpdateTotalCost() ;
    // }

    // // If extra exists,
    // {
    //     let extraNodes = document.getElementsByClassName('extrasub') ;
    //     for ( let i = 0 ; i < extraNodes.length ; i++)
    //     {
    //         extraNodes[i].addEventListener ( 'change' , fnUpdateForExtraCost , false ) ;
    //     }
    // }
});

