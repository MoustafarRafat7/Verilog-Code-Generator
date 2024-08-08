module pwm_basic 
#(parameter R=8)
(
input clk, 
input reset, 
input [R-1:0] duty, 
output wire pwm_out
); 

always@( posedge clk , negedge reset)
begin
if(!reset)
begin

end
else
begin

end
endmodule