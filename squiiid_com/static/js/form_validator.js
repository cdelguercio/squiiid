var addedfile = false

function upload_validate() {
	return addedfile;
}

(function(){
	$(document).ready(function(){
		// validate upload form
		$('#upload-form').validate({
			rules: {
				tags: {
					required: true,
				}
			}
		});
	});
	
	
	
	
	/*
	var MIN_QUOTE_AMOUNT = 7
	var MIN_TURNAROUND_DAYS = 2
	MIN_EXPIRATION_DAYS = 0
	
	states = new Array(	"AL","AR","AZ","CA","CO","CT","DC","DE","FL","GA","IA","ID","IL","IN","KS","KY","LA",
						"MA","MD","ME","MH","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY",
						"OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VA","VT","WA","WI","WV","WY");

	jQuery.validator.addMethod("currency", function(value, element){
		is_currency = true
		my_number = parseFloat(value.replace(/\$/,'').replace(/\,/g,''))
		if( Number.isNaN(my_number) || my_number < 0 ) {
			is_currency = false
		}
		return this.optional(element) || is_currency;
	}, "Please enter an amount in US dollars");

	jQuery.validator.addMethod("total_check", function(value, element){
		is_valid_amount = true
		my_number = parseFloat(value.replace(/\$/,'').replace(/\,/g,''))
		if( !NumberisNaN(my_number) && (my_number >= MIN_QUOTE_AMOUNT) ) {
			is_valid_amount = false
		}
		return this.optional(element) || is_valid_amount;
	}, "Please make sure that you are quoting for the total order and not per shirt");

	jQuery.validator.addMethod("required_turnaround_date_future_check", function(value, element){
		date_valid = true
		day = $('#day').val()
		month = $('#month').val() - 1 //the month in the form starts at 1 and the javascript month starts at 0
		year = $('#year').val()
		if( day == '' || month == '' || year == '') {
			return this.optional(element) || date_valid;
		}
		now = new Date()
		required_turnaround_date = new Date(year,month,day)
		if( required_turnaround_date.getTime() < now.getTime() + (MIN_TURNAROUND_DAYS * 86400000) ) {
			date_valid = false
		}
		return this.optional(element) || date_valid;
	}, "Please select a date that is more than " + MIN_TURNAROUND_DAYS.toString() + " days in the future");
	
	jQuery.validator.addMethod("bid_expiration_date_future_check", function(value, element){
		date_valid = true
		day = $('#day').val()
		month = $('#month').val() - 1 //the month in the form starts at 1 and the javascript month starts at 0
		year = $('#year').val()
		if( day == '' || month == '' || year == '') {
			return this.optional(element) || date_valid;
		}
		now = new Date()
		required_turnaround_date = new Date(year,month,day)
		if( required_turnaround_date.getTime() < now.getTime() + (MIN_EXPIRATION_DAYS * 86400000) ) {
			date_valid = false
		}
		return this.optional(element) || date_valid;
	}, "Please select a date that is more than " + MIN_EXPIRATION_DAYS.toString() + " days in the future");
	
	jQuery.validator.addMethod("date_valid_check", function(value, element){
		date_valid = true
		day = $('#day').val()
		month = $('#month').val() - 1 //the month in the form starts at 1 and the javascript month starts at 0
		year = $('#year').val()
		if( day == '' || month == '' || year == '') {
			return this.optional(element) || date_valid;
		}
		required_turnaround_date = new Date(year,month,day)
		if( month != required_turnaround_date.getMonth() ) {
			date_valid = false
		}
		return this.optional(element) || date_valid;
	}, "Please select a day that exists within your selected month");
	
	jQuery.validator.addMethod("state_valid_check", function(value, element){
		is_state = false
		state = $('#state').val().toUpperCase()
		var length = states.length;
		for(var i = 0; i < length; i++) {
			if(states[i] == state){
				is_state = true;
			}
		}
		return this.optional(element) || is_state;
	}, "Please enter a valid state");
	
	jQuery.validator.addMethod("printer_state_valid_check", function(value, element){
		is_state = false
		state = $('#id_printer_state').val().toUpperCase()
		var length = states.length;
		for(var i = 0; i < length; i++) {
			if(states[i] == state){
				is_state = true;
			}
		}
		
		return this.optional(element) || is_state;
	}, "Please enter a valid state");
  
	var defaultOptions = {
		email: {
			required: true,
			email: true
		},
		password1: 'required',
		password2: {
    		equalTo: '#id_password1'
		},
		printer_name: 'required',
		printer_contact_name: 'required',
		printer_street_address_1: 'required',
		printer_city: 'required',
		printer_state: {
			required: true,
			printer_state_valid_check: true
		},
		printer_zip_code: 'required',
		printer_phone_number: 'required'
	};

	$(document).ready(function(){
		// validate customer sign up
		$('.j_customer_signup').validate({
	    	rules: defaultOptions
		});
		//
		// validate printer sign up
		$('.j_printer_signup').validate({
	    	rules: defaultOptions,
	    	errorPlacement: function(error, element) {
				if(element.attr("name") == "printer_state")
					error.insertAfter(".input_group");
				else
					error.insertAfter(element);
			}
		});
		//
		// validate order details
		$('.j_order_details').validate({
			rules: {
				day: {
					required: true,
					required_turnaround_date_future_check: true,
					date_valid_check: true
				},
				month: {
					required: true,
					required_turnaround_date_future_check: true,
					date_valid_check: true
				},
				year: {
					required: true,
					required_turnaround_date_future_check: true,
					date_valid_check: true
				},
				name: "required",
				city: "required",
				state: {
					required: true,
					state_valid_check: true
				},
				zip_code: {
					required: true,
					number: true
				}
			},
			groups: {
				full_date: "day month year"
			},
			errorPlacement: function(error, element) {
				if (element.attr("name") == "day" || element.attr("name") == "month" || element.attr("name") == "year") 
					error.insertAfter("#full_date");
				else if(element.attr("name") == "state")
					error.insertAfter(".cityStateZip");
				else
					error.insertAfter(element);
			}
		});
		//
		// validate bid form
		$('.bid_form').validate({
			rules: {
				day: {
					required: true,
					bid_expiration_date_future_check: true,
					date_valid_check: true
				},
				month: {
					required: true,
					bid_expiration_date_future_check: true,
					date_valid_check: true
				},
				year: {
					required: true,
					bid_expiration_date_future_check: true,
					date_valid_check: true
				},
				amount: {
					required: true,
					currency: true//, //TODO
					//total_check: true
				}
			},
			groups: {
				full_date: "day month year"
			},
			errorPlacement: function(error, element) {
				if (element.attr("name") == "day" || element.attr("name") == "month" || element.attr("name") == "year") 
					error.insertAfter("#full_date");
				else
					error.insertAfter(element);
			}
		});
	});*/
}).call(this);
