module mux_8x1_nbit_TB
();
localparam N=3;
reg [N-1:0] w0_TB;
reg [N-1:0] w1_TB;
reg [N-1:0] w2_TB;
reg [N-1:0] w3_TB;
reg [N-1:0] w4_TB;
reg [N-1:0] w5_TB;
reg [N-1:0] w6_TB;
reg [N-1:0] w7_TB;
reg [2:0] s_TB;
wire [N-1:0]f_TB;
mux_8x1_nbit #(.N(N)) mux_8x1_nbit_TB (.w0(w0_TB),.w1(w1_TB),.w2(w2_TB),.w3(w3_TB),.w4(w4_TB),.w5(w5_TB),.w6(w6_TB),.w7(w7_TB),.s(s_TB),.f(f_TB) );

initial
begin




end

endmodule