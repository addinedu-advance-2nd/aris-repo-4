// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_msgs:msg/UserOrder.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__USER_ORDER__BUILDER_HPP_
#define ROBOT_MSGS__MSG__DETAIL__USER_ORDER__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robot_msgs/msg/detail/user_order__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robot_msgs
{

namespace msg
{

namespace builder
{

class Init_UserOrder_topping_type
{
public:
  explicit Init_UserOrder_topping_type(::robot_msgs::msg::UserOrder & msg)
  : msg_(msg)
  {}
  ::robot_msgs::msg::UserOrder topping_type(::robot_msgs::msg::UserOrder::_topping_type_type arg)
  {
    msg_.topping_type = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::msg::UserOrder msg_;
};

class Init_UserOrder_topping
{
public:
  explicit Init_UserOrder_topping(::robot_msgs::msg::UserOrder & msg)
  : msg_(msg)
  {}
  Init_UserOrder_topping_type topping(::robot_msgs::msg::UserOrder::_topping_type arg)
  {
    msg_.topping = std::move(arg);
    return Init_UserOrder_topping_type(msg_);
  }

private:
  ::robot_msgs::msg::UserOrder msg_;
};

class Init_UserOrder_icecream
{
public:
  explicit Init_UserOrder_icecream(::robot_msgs::msg::UserOrder & msg)
  : msg_(msg)
  {}
  Init_UserOrder_topping icecream(::robot_msgs::msg::UserOrder::_icecream_type arg)
  {
    msg_.icecream = std::move(arg);
    return Init_UserOrder_topping(msg_);
  }

private:
  ::robot_msgs::msg::UserOrder msg_;
};

class Init_UserOrder_action
{
public:
  Init_UserOrder_action()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_UserOrder_icecream action(::robot_msgs::msg::UserOrder::_action_type arg)
  {
    msg_.action = std::move(arg);
    return Init_UserOrder_icecream(msg_);
  }

private:
  ::robot_msgs::msg::UserOrder msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::msg::UserOrder>()
{
  return robot_msgs::msg::builder::Init_UserOrder_action();
}

}  // namespace robot_msgs

#endif  // ROBOT_MSGS__MSG__DETAIL__USER_ORDER__BUILDER_HPP_
