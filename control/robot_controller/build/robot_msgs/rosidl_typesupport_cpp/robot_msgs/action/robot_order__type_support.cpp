// generated from rosidl_typesupport_cpp/resource/idl__type_support.cpp.em
// with input from robot_msgs:action/RobotOrder.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "robot_msgs/action/detail/robot_order__struct.hpp"
#include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
#include "rosidl_typesupport_cpp/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace robot_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _RobotOrder_Goal_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _RobotOrder_Goal_type_support_ids_t;

static const _RobotOrder_Goal_type_support_ids_t _RobotOrder_Goal_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _RobotOrder_Goal_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _RobotOrder_Goal_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _RobotOrder_Goal_type_support_symbol_names_t _RobotOrder_Goal_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, robot_msgs, action, RobotOrder_Goal)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, robot_msgs, action, RobotOrder_Goal)),
  }
};

typedef struct _RobotOrder_Goal_type_support_data_t
{
  void * data[2];
} _RobotOrder_Goal_type_support_data_t;

static _RobotOrder_Goal_type_support_data_t _RobotOrder_Goal_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _RobotOrder_Goal_message_typesupport_map = {
  2,
  "robot_msgs",
  &_RobotOrder_Goal_message_typesupport_ids.typesupport_identifier[0],
  &_RobotOrder_Goal_message_typesupport_symbol_names.symbol_name[0],
  &_RobotOrder_Goal_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t RobotOrder_Goal_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_RobotOrder_Goal_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace robot_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<robot_msgs::action::RobotOrder_Goal>()
{
  return &::robot_msgs::action::rosidl_typesupport_cpp::RobotOrder_Goal_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, robot_msgs, action, RobotOrder_Goal)() {
  return get_message_type_support_handle<robot_msgs::action::RobotOrder_Goal>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "robot_msgs/action/detail/robot_order__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace robot_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _RobotOrder_Result_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _RobotOrder_Result_type_support_ids_t;

static const _RobotOrder_Result_type_support_ids_t _RobotOrder_Result_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _RobotOrder_Result_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _RobotOrder_Result_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _RobotOrder_Result_type_support_symbol_names_t _RobotOrder_Result_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, robot_msgs, action, RobotOrder_Result)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, robot_msgs, action, RobotOrder_Result)),
  }
};

typedef struct _RobotOrder_Result_type_support_data_t
{
  void * data[2];
} _RobotOrder_Result_type_support_data_t;

static _RobotOrder_Result_type_support_data_t _RobotOrder_Result_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _RobotOrder_Result_message_typesupport_map = {
  2,
  "robot_msgs",
  &_RobotOrder_Result_message_typesupport_ids.typesupport_identifier[0],
  &_RobotOrder_Result_message_typesupport_symbol_names.symbol_name[0],
  &_RobotOrder_Result_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t RobotOrder_Result_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_RobotOrder_Result_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace robot_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<robot_msgs::action::RobotOrder_Result>()
{
  return &::robot_msgs::action::rosidl_typesupport_cpp::RobotOrder_Result_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, robot_msgs, action, RobotOrder_Result)() {
  return get_message_type_support_handle<robot_msgs::action::RobotOrder_Result>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "robot_msgs/action/detail/robot_order__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace robot_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _RobotOrder_Feedback_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _RobotOrder_Feedback_type_support_ids_t;

static const _RobotOrder_Feedback_type_support_ids_t _RobotOrder_Feedback_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _RobotOrder_Feedback_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _RobotOrder_Feedback_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _RobotOrder_Feedback_type_support_symbol_names_t _RobotOrder_Feedback_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, robot_msgs, action, RobotOrder_Feedback)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, robot_msgs, action, RobotOrder_Feedback)),
  }
};

typedef struct _RobotOrder_Feedback_type_support_data_t
{
  void * data[2];
} _RobotOrder_Feedback_type_support_data_t;

static _RobotOrder_Feedback_type_support_data_t _RobotOrder_Feedback_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _RobotOrder_Feedback_message_typesupport_map = {
  2,
  "robot_msgs",
  &_RobotOrder_Feedback_message_typesupport_ids.typesupport_identifier[0],
  &_RobotOrder_Feedback_message_typesupport_symbol_names.symbol_name[0],
  &_RobotOrder_Feedback_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t RobotOrder_Feedback_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_RobotOrder_Feedback_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace robot_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<robot_msgs::action::RobotOrder_Feedback>()
{
  return &::robot_msgs::action::rosidl_typesupport_cpp::RobotOrder_Feedback_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, robot_msgs, action, RobotOrder_Feedback)() {
  return get_message_type_support_handle<robot_msgs::action::RobotOrder_Feedback>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "robot_msgs/action/detail/robot_order__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace robot_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _RobotOrder_SendGoal_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _RobotOrder_SendGoal_Request_type_support_ids_t;

static const _RobotOrder_SendGoal_Request_type_support_ids_t _RobotOrder_SendGoal_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _RobotOrder_SendGoal_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _RobotOrder_SendGoal_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _RobotOrder_SendGoal_Request_type_support_symbol_names_t _RobotOrder_SendGoal_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, robot_msgs, action, RobotOrder_SendGoal_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, robot_msgs, action, RobotOrder_SendGoal_Request)),
  }
};

typedef struct _RobotOrder_SendGoal_Request_type_support_data_t
{
  void * data[2];
} _RobotOrder_SendGoal_Request_type_support_data_t;

static _RobotOrder_SendGoal_Request_type_support_data_t _RobotOrder_SendGoal_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _RobotOrder_SendGoal_Request_message_typesupport_map = {
  2,
  "robot_msgs",
  &_RobotOrder_SendGoal_Request_message_typesupport_ids.typesupport_identifier[0],
  &_RobotOrder_SendGoal_Request_message_typesupport_symbol_names.symbol_name[0],
  &_RobotOrder_SendGoal_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t RobotOrder_SendGoal_Request_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_RobotOrder_SendGoal_Request_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace robot_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<robot_msgs::action::RobotOrder_SendGoal_Request>()
{
  return &::robot_msgs::action::rosidl_typesupport_cpp::RobotOrder_SendGoal_Request_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, robot_msgs, action, RobotOrder_SendGoal_Request)() {
  return get_message_type_support_handle<robot_msgs::action::RobotOrder_SendGoal_Request>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "robot_msgs/action/detail/robot_order__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace robot_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _RobotOrder_SendGoal_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _RobotOrder_SendGoal_Response_type_support_ids_t;

static const _RobotOrder_SendGoal_Response_type_support_ids_t _RobotOrder_SendGoal_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _RobotOrder_SendGoal_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _RobotOrder_SendGoal_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _RobotOrder_SendGoal_Response_type_support_symbol_names_t _RobotOrder_SendGoal_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, robot_msgs, action, RobotOrder_SendGoal_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, robot_msgs, action, RobotOrder_SendGoal_Response)),
  }
};

typedef struct _RobotOrder_SendGoal_Response_type_support_data_t
{
  void * data[2];
} _RobotOrder_SendGoal_Response_type_support_data_t;

static _RobotOrder_SendGoal_Response_type_support_data_t _RobotOrder_SendGoal_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _RobotOrder_SendGoal_Response_message_typesupport_map = {
  2,
  "robot_msgs",
  &_RobotOrder_SendGoal_Response_message_typesupport_ids.typesupport_identifier[0],
  &_RobotOrder_SendGoal_Response_message_typesupport_symbol_names.symbol_name[0],
  &_RobotOrder_SendGoal_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t RobotOrder_SendGoal_Response_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_RobotOrder_SendGoal_Response_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace robot_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<robot_msgs::action::RobotOrder_SendGoal_Response>()
{
  return &::robot_msgs::action::rosidl_typesupport_cpp::RobotOrder_SendGoal_Response_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, robot_msgs, action, RobotOrder_SendGoal_Response)() {
  return get_message_type_support_handle<robot_msgs::action::RobotOrder_SendGoal_Response>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "robot_msgs/action/detail/robot_order__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/service_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace robot_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _RobotOrder_SendGoal_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _RobotOrder_SendGoal_type_support_ids_t;

static const _RobotOrder_SendGoal_type_support_ids_t _RobotOrder_SendGoal_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _RobotOrder_SendGoal_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _RobotOrder_SendGoal_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _RobotOrder_SendGoal_type_support_symbol_names_t _RobotOrder_SendGoal_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, robot_msgs, action, RobotOrder_SendGoal)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, robot_msgs, action, RobotOrder_SendGoal)),
  }
};

typedef struct _RobotOrder_SendGoal_type_support_data_t
{
  void * data[2];
} _RobotOrder_SendGoal_type_support_data_t;

static _RobotOrder_SendGoal_type_support_data_t _RobotOrder_SendGoal_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _RobotOrder_SendGoal_service_typesupport_map = {
  2,
  "robot_msgs",
  &_RobotOrder_SendGoal_service_typesupport_ids.typesupport_identifier[0],
  &_RobotOrder_SendGoal_service_typesupport_symbol_names.symbol_name[0],
  &_RobotOrder_SendGoal_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t RobotOrder_SendGoal_service_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_RobotOrder_SendGoal_service_typesupport_map),
  ::rosidl_typesupport_cpp::get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace robot_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<robot_msgs::action::RobotOrder_SendGoal>()
{
  return &::robot_msgs::action::rosidl_typesupport_cpp::RobotOrder_SendGoal_service_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "robot_msgs/action/detail/robot_order__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace robot_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _RobotOrder_GetResult_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _RobotOrder_GetResult_Request_type_support_ids_t;

static const _RobotOrder_GetResult_Request_type_support_ids_t _RobotOrder_GetResult_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _RobotOrder_GetResult_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _RobotOrder_GetResult_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _RobotOrder_GetResult_Request_type_support_symbol_names_t _RobotOrder_GetResult_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, robot_msgs, action, RobotOrder_GetResult_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, robot_msgs, action, RobotOrder_GetResult_Request)),
  }
};

typedef struct _RobotOrder_GetResult_Request_type_support_data_t
{
  void * data[2];
} _RobotOrder_GetResult_Request_type_support_data_t;

static _RobotOrder_GetResult_Request_type_support_data_t _RobotOrder_GetResult_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _RobotOrder_GetResult_Request_message_typesupport_map = {
  2,
  "robot_msgs",
  &_RobotOrder_GetResult_Request_message_typesupport_ids.typesupport_identifier[0],
  &_RobotOrder_GetResult_Request_message_typesupport_symbol_names.symbol_name[0],
  &_RobotOrder_GetResult_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t RobotOrder_GetResult_Request_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_RobotOrder_GetResult_Request_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace robot_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<robot_msgs::action::RobotOrder_GetResult_Request>()
{
  return &::robot_msgs::action::rosidl_typesupport_cpp::RobotOrder_GetResult_Request_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, robot_msgs, action, RobotOrder_GetResult_Request)() {
  return get_message_type_support_handle<robot_msgs::action::RobotOrder_GetResult_Request>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "robot_msgs/action/detail/robot_order__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace robot_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _RobotOrder_GetResult_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _RobotOrder_GetResult_Response_type_support_ids_t;

static const _RobotOrder_GetResult_Response_type_support_ids_t _RobotOrder_GetResult_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _RobotOrder_GetResult_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _RobotOrder_GetResult_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _RobotOrder_GetResult_Response_type_support_symbol_names_t _RobotOrder_GetResult_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, robot_msgs, action, RobotOrder_GetResult_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, robot_msgs, action, RobotOrder_GetResult_Response)),
  }
};

typedef struct _RobotOrder_GetResult_Response_type_support_data_t
{
  void * data[2];
} _RobotOrder_GetResult_Response_type_support_data_t;

static _RobotOrder_GetResult_Response_type_support_data_t _RobotOrder_GetResult_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _RobotOrder_GetResult_Response_message_typesupport_map = {
  2,
  "robot_msgs",
  &_RobotOrder_GetResult_Response_message_typesupport_ids.typesupport_identifier[0],
  &_RobotOrder_GetResult_Response_message_typesupport_symbol_names.symbol_name[0],
  &_RobotOrder_GetResult_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t RobotOrder_GetResult_Response_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_RobotOrder_GetResult_Response_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace robot_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<robot_msgs::action::RobotOrder_GetResult_Response>()
{
  return &::robot_msgs::action::rosidl_typesupport_cpp::RobotOrder_GetResult_Response_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, robot_msgs, action, RobotOrder_GetResult_Response)() {
  return get_message_type_support_handle<robot_msgs::action::RobotOrder_GetResult_Response>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "robot_msgs/action/detail/robot_order__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/service_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace robot_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _RobotOrder_GetResult_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _RobotOrder_GetResult_type_support_ids_t;

static const _RobotOrder_GetResult_type_support_ids_t _RobotOrder_GetResult_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _RobotOrder_GetResult_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _RobotOrder_GetResult_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _RobotOrder_GetResult_type_support_symbol_names_t _RobotOrder_GetResult_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, robot_msgs, action, RobotOrder_GetResult)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, robot_msgs, action, RobotOrder_GetResult)),
  }
};

typedef struct _RobotOrder_GetResult_type_support_data_t
{
  void * data[2];
} _RobotOrder_GetResult_type_support_data_t;

static _RobotOrder_GetResult_type_support_data_t _RobotOrder_GetResult_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _RobotOrder_GetResult_service_typesupport_map = {
  2,
  "robot_msgs",
  &_RobotOrder_GetResult_service_typesupport_ids.typesupport_identifier[0],
  &_RobotOrder_GetResult_service_typesupport_symbol_names.symbol_name[0],
  &_RobotOrder_GetResult_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t RobotOrder_GetResult_service_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_RobotOrder_GetResult_service_typesupport_map),
  ::rosidl_typesupport_cpp::get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace robot_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<robot_msgs::action::RobotOrder_GetResult>()
{
  return &::robot_msgs::action::rosidl_typesupport_cpp::RobotOrder_GetResult_service_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "robot_msgs/action/detail/robot_order__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace robot_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

typedef struct _RobotOrder_FeedbackMessage_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _RobotOrder_FeedbackMessage_type_support_ids_t;

static const _RobotOrder_FeedbackMessage_type_support_ids_t _RobotOrder_FeedbackMessage_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _RobotOrder_FeedbackMessage_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _RobotOrder_FeedbackMessage_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _RobotOrder_FeedbackMessage_type_support_symbol_names_t _RobotOrder_FeedbackMessage_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, robot_msgs, action, RobotOrder_FeedbackMessage)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, robot_msgs, action, RobotOrder_FeedbackMessage)),
  }
};

typedef struct _RobotOrder_FeedbackMessage_type_support_data_t
{
  void * data[2];
} _RobotOrder_FeedbackMessage_type_support_data_t;

static _RobotOrder_FeedbackMessage_type_support_data_t _RobotOrder_FeedbackMessage_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _RobotOrder_FeedbackMessage_message_typesupport_map = {
  2,
  "robot_msgs",
  &_RobotOrder_FeedbackMessage_message_typesupport_ids.typesupport_identifier[0],
  &_RobotOrder_FeedbackMessage_message_typesupport_symbol_names.symbol_name[0],
  &_RobotOrder_FeedbackMessage_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t RobotOrder_FeedbackMessage_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_RobotOrder_FeedbackMessage_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace robot_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<robot_msgs::action::RobotOrder_FeedbackMessage>()
{
  return &::robot_msgs::action::rosidl_typesupport_cpp::RobotOrder_FeedbackMessage_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, robot_msgs, action, RobotOrder_FeedbackMessage)() {
  return get_message_type_support_handle<robot_msgs::action::RobotOrder_FeedbackMessage>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

#include "action_msgs/msg/goal_status_array.hpp"
#include "action_msgs/srv/cancel_goal.hpp"
// already included above
// #include "robot_msgs/action/detail/robot_order__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
#include "rosidl_runtime_c/action_type_support_struct.h"
#include "rosidl_typesupport_cpp/action_type_support.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_cpp/service_type_support.hpp"

namespace robot_msgs
{

namespace action
{

namespace rosidl_typesupport_cpp
{

static rosidl_action_type_support_t RobotOrder_action_type_support_handle = {
  NULL, NULL, NULL, NULL, NULL};

}  // namespace rosidl_typesupport_cpp

}  // namespace action

}  // namespace robot_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_action_type_support_t *
get_action_type_support_handle<robot_msgs::action::RobotOrder>()
{
  using ::robot_msgs::action::rosidl_typesupport_cpp::RobotOrder_action_type_support_handle;
  // Thread-safe by always writing the same values to the static struct
  RobotOrder_action_type_support_handle.goal_service_type_support = get_service_type_support_handle<::robot_msgs::action::RobotOrder::Impl::SendGoalService>();
  RobotOrder_action_type_support_handle.result_service_type_support = get_service_type_support_handle<::robot_msgs::action::RobotOrder::Impl::GetResultService>();
  RobotOrder_action_type_support_handle.cancel_service_type_support = get_service_type_support_handle<::robot_msgs::action::RobotOrder::Impl::CancelGoalService>();
  RobotOrder_action_type_support_handle.feedback_message_type_support = get_message_type_support_handle<::robot_msgs::action::RobotOrder::Impl::FeedbackMessage>();
  RobotOrder_action_type_support_handle.status_message_type_support = get_message_type_support_handle<::robot_msgs::action::RobotOrder::Impl::GoalStatusMessage>();
  return &RobotOrder_action_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp