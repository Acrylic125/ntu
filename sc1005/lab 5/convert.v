module convert(input [3:0] index, output reg [3:0] selnum);
    always @* begin 
        case (index)
            4'd0: selnum = 4'hA; // Space
            4'd1: selnum = 4'hA; // Space
            4'd2: selnum = 4'hC;
            4'd3: selnum = 4'h0;
            4'd4: selnum = 4'hf;
            4'd5: selnum = 4'hf;
            4'd6: selnum = 4'he;
            4'd7: selnum = 4'he;
            4'd8: selnum = 4'hA; // Space
            4'd9: selnum = 4'h1;
            4'd10: selnum = 4'h5;
            4'd11: selnum = 4'hA;
            4'd12: selnum = 4'h9;
            4'd13: selnum = 4'hb; // Lowercase o
            4'd14: selnum = 4'hb; // Lowercase o
            4'd15: selnum = 4'hd;
            default: selnum = 4'hA; // Default to space
        endcase
    end
endmodule