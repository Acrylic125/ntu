module scroll(input clk, rst, output [15:0] display);
    reg [3:0] counter;
    
    wire [3:0] a, b, c, d;
    assign a = counter;
    assign b = counter + 1;
    assign c = counter + 2;
    assign d = counter + 3;
    
    wire [3:0] converted_a, converted_b, converted_c, converted_d;
    convert conv_a(.index(a), .selnum(converted_a));
    convert conv_b(.index(b), .selnum(converted_b));
    convert conv_c(.index(c), .selnum(converted_c));
    convert conv_d(.index(d), .selnum(converted_d));

    assign display = {converted_a, converted_b, converted_c, converted_d};

    always @(posedge clk) begin 
        if (rst)
            counter <= 4'b0;
        else 
            counter <= counter + 1;
    end
endmodule