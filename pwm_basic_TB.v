module pwm_basic_TB
();
localparam R=8;
reg clk_TB;
reg reset_TB;
reg [R-1:0] duty_TB;
wire pwm_out_TB;
pwm_basic #(.R(R)) pwm_basic_TB (.clk(clk_TB),.reset(reset_TB),.duty(duty_TB),.pwm_out(pwm_out_TB) );

always
begin




end

initial
begin




end

endmodule