// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from robot_msgs:msg/UserOrder.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__USER_ORDER__TRAITS_HPP_
#define ROBOT_MSGS__MSG__DETAIL__USER_ORDER__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "robot_msgs/msg/detail/user_order__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace robot_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const UserOrder & msg,
  std::ostream & out)
{
  out << "{";
  // member: action
  {
    out << "action: ";
    rosidl_generator_traits::value_to_yaml(msg.action, out);
    out << ", ";
  }

  // member: icecream
  {
    out << "icecream: ";
    rosidl_generator_traits::value_to_yaml(msg.icecream, out);
    out << ", ";
  }

  // member: topping
  {
    out << "topping: ";
    rosidl_generator_traits::value_to_yaml(msg.topping, out);
    out << ", ";
  }

  // member: topping_type
  {
    out << "topping_type: ";
    rosidl_generator_traits::value_to_yaml(msg.topping_type, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const UserOrder & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: action
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "action: ";
    rosidl_generator_traits::value_to_yaml(msg.action, out);
    out << "\n";
  }

  // member: icecream
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "icecream: ";
    rosidl_generator_traits::value_to_yaml(msg.icecream, out);
    out << "\n";
  }

  // member: topping
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "topping: ";
    rosidl_generator_traits::value_to_yaml(msg.topping, out);
    out << "\n";
  }

  // member: topping_type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "topping_type: ";
    rosidl_generator_traits::value_to_yaml(msg.topping_type, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const UserOrder & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace robot_msgs

namespace rosidl_generator_traits
{

[[deprecated("use robot_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robot_msgs::msg::UserOrder & msg,
  std::ostream & out, size_t indentation = 0)
{
  robot_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robot_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const robot_msgs::msg::UserOrder & msg)
{
  return robot_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<robot_msgs::msg::UserOrder>()
{
  return "robot_msgs::msg::UserOrder";
}

template<>
inline const char * name<robot_msgs::msg::UserOrder>()
{
  return "robot_msgs/msg/UserOrder";
}

template<>
struct has_fixed_size<robot_msgs::msg::UserOrder>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<robot_msgs::msg::UserOrder>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<robot_msgs::msg::UserOrder>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ROBOT_MSGS__MSG__DETAIL__USER_ORDER__TRAITS_HPP_
